console.error("DOWNLOAD.JS LOADED SUCCESSFULLY");
document.addEventListener("click", async function (event) {
    const link = event.target.closest("a.download-file");

    if (!link) return;
    
    console.error("DOWNLOAD HANDLER TRIGGERED:", link.href);
    
    event.preventDefault();

    const fileUrl = link.href;
    const fileName = link.dataset.filename || "download";

    try {
        const response = await fetch(fileUrl);

        if (!response.ok) {
            throw new Error(`Download failed: ${response.status}`);
        }

        const blob = await response.blob();
        const downloadUrl = URL.createObjectURL(blob);

        const downloadLink = document.createElement("a");
        downloadLink.href = downloadUrl;
        downloadLink.download = fileName;

        document.body.appendChild(downloadLink);
        downloadLink.click();
        downloadLink.remove();

        setTimeout(() => {
            URL.revokeObjectURL(downloadUrl);
        }, 30000);

    } catch (error) {
        console.error("Download error:", error);
        alert("Unable to download the file. Please try again.");
    }
});
