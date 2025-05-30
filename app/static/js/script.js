function openModal(id) {
    document.getElementById(id).style.display = "block";
}

function closeModal(id) {
    document.getElementById(id).style.display = "none";
}

// Fermer si clic hors de la modale
window.onclick = function(event) {
    ['uploadModal', 'openModal'].forEach(id => {
        const modal = document.getElementById(id);
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
};

// ✅ Ouvrir automatiquement la modale si un message flash est présent
window.onload = function () {
    const flash = document.querySelector('.flash-messages-modal');
    if (flash) {
        openModal('uploadModal');
    }
};

// Bloquer les fichiers .tif avant l'envoi
document.addEventListener("DOMContentLoaded", function () {
    const uploadForm = document.querySelector('form[action="/upload-mosaique"]');
    if (uploadForm) {
        uploadForm.addEventListener("submit", function (e) {
            const input = uploadForm.querySelector('input[type="file"]');
            const file = input.files[0];
            if (file) {
                const ext = file.name.split('.').pop().toLowerCase();
                if (ext === 'tif' || ext === 'tiff') {
                    e.preventDefault();

                    const errorDiv = document.getElementById("client-error");
                    errorDiv.innerText = "❌ Le format TIF/TIFF est interdit. Utilisez un fichier JPG, JPEG ou PNG.";
                    errorDiv.style.display = "block";
                }

            }
        });
    }
});
