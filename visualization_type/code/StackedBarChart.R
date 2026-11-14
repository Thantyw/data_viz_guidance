# Reproducible ACS S2701 100% Stacked Bar Chart
#
# Source:
#   U.S. Census Bureau, American Community Survey (ACS),
#   2020-2024 5-Year Estimates, Subject Table S2701,
#   Selected Characteristics of Health Insurance Coverage
#   in the United States.
#
# Universe:
#   Civilian noninstitutionalized population.
#
# Measures:
#   Percentage with health insurance coverage.
#   Percentage without health insurance coverage.
#
# Geographies:
#   Delaware, District of Columbia, Maryland,
#   Pennsylvania, and Virginia.
#
# Input:
#   visualization_type/data/ACSST5Y2024.S2701-Data.csv
#
# Output:
#   visualization_type/assets/StackedBarChart1_R.png
#
# This script reads the versioned Census flat CSV stored in the
# visualization_type/data directory. Missing or unavailable values
# are not replaced with zero.


# ---------------------------------------------------------------------
# File locations
# ---------------------------------------------------------------------

# Determine the location of this script when executed with Rscript.
command_args <- commandArgs(
  trailingOnly = FALSE
)

file_arg <- grep(
  "^--file=",
  command_args,
  value = TRUE
)

if (length(file_arg) != 1) {
  stop(
    "Unable to determine the location of StackedBarChart.R."
  )
}

script_file <- normalizePath(
  sub(
    "^--file=",
    "",
    file_arg
  ),
  mustWork = TRUE
)

# This script is stored in visualization_type/code/.
code_dir <- dirname(
  script_file
)

# The parent directory contains the guidance pages, data, and assets.
visualization_dir <- dirname(
  code_dir
)

data_file <- file.path(
  visualization_dir,
  "data",
  "ACSST5Y2024.S2701-Data.csv"
)

output_file <- file.path(
  visualization_dir,
  "assets",
  "StackedBarChart1_R.png"
)
