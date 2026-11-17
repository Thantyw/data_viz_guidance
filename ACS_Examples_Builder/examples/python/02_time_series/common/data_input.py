"""GB-DATA-001 shared input adapter. No API calls in local modes.

Supported local input is a tidy table containing `year`, Census variable codes and
`NAME` (full state name). Census API access is delegated to a chart-specific callable.
Local records must document their true source; this loader does not attest provenance.
"""
from __future__ import annotations
import os
from pathlib import Path
import pandas as pd

SOURCES = {'api', 'csv', 'excel', 'dataframe'}


def read_local(source: str, *, input_file=None, dataframe=None, required=(), years=None) -> pd.DataFrame:
    """Load analyst data without touching any network or requiring credentials."""
    if source not in {'csv', 'excel', 'dataframe'}:
        raise ValueError('Local input source must be csv, excel, or dataframe')
    if source == 'dataframe':
        if not isinstance(dataframe, pd.DataFrame):
            raise TypeError('For source=dataframe, supply a pandas DataFrame')
        df = dataframe.copy(deep=True)
    else:
        if input_file is None:
            raise ValueError(f'source={source} requires --input-file or input_file')
        path = Path(input_file).expanduser()
        if not path.is_file():
            raise FileNotFoundError(f'Input file does not exist: {path}')
        if source == 'csv':
            df = pd.read_csv(path, dtype={'state': str, 'state_fips': str})
        else:
            df = pd.read_excel(path, dtype={'state': str, 'state_fips': str})
    needed = set(required) | {'year'}
    absent = sorted(needed - set(df.columns))
    if absent:
        raise ValueError(f'Input is missing required columns: {absent}')
    df['year'] = pd.to_numeric(df['year'], errors='raise')
    if df['year'].isna().any() or (df['year'] % 1 != 0).any():
        raise ValueError('Input year must be a whole number for every record')
    df['year'] = df['year'].astype(int)
    if years is not None:
        df = df.loc[df['year'].isin([int(y) for y in years])].copy()
        if df.empty:
            raise ValueError('None of the requested years are present in local data')
    return df.reset_index(drop=True)


def yearly_frames(source: str, years, required, *, api_loader=None, input_file=None, dataframe=None):
    """Return one frame per year. Only source='api' can invoke api_loader."""
    source = source.strip().lower()
    if source not in SOURCES:
        raise ValueError(f'Unsupported data source {source!r}; choose {sorted(SOURCES)}')
    years = list(years)
    if source == 'api':
        if api_loader is None:
            raise ValueError('API mode requires a chart-specific fetch function')
        frames = [pd.DataFrame(api_loader(y)).copy() for y in years]
    else:
        all_data = read_local(source, input_file=input_file, dataframe=dataframe,
                              required=required, years=years)
        frames = [all_data.loc[all_data['year'].eq(y)].copy() for y in years]
    for y, frame in zip(years, frames):
        if frame.empty:
            raise ValueError(f'No records available for requested year {y}')
        missing = set(required) - set(frame.columns)
        if missing:
            raise ValueError(f'Year {y} is missing columns: {sorted(missing)}')
    return frames


def source_description(source, input_file=None):
    return {'input_mode': source,
            'local_input': str(Path(input_file).expanduser().resolve()) if input_file and source != 'api' else None,
            'credentials_saved': False,
            'source_provenance': 'Analyst-provided; verify metadata for local inputs' if source != 'api' else 'Census API'}
