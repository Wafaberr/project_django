 
 
 
 
 // Solution équilibrée recommandée
let unsavedChanges = false;

// Détecter les modifications
document.addEventListener('change', function(e) {
    if (e.target.matches('form input, form textarea, form select')) {
        unsavedChanges = true;
    }
});

// Confirmation avant de quitter
window.addEventListener('beforeunload', function(e) {
    if (unsavedChanges) {
        // Le message sera généré par le navigateur
        e.preventDefault();
        e.returnValue = '';
        return '';
    }
});

// Réinitialiser après sauvegarde/soumission
document.querySelector('form')?.addEventListener('submit', function() {
    unsavedChanges = false;
});

// Permettre le rafraîchissement programmatique
function safeRefresh() {
    unsavedChanges = false;
    window.location.reload();
}
 
 
 

 
 
 
 
 // Validation des champs requis
        document.addEventListener('DOMContentLoaded', function () {
            const form = document.querySelector('form');
            form.addEventListener('submit', function (event) {
                let isValid = true;
                const requiredFields = form.querySelectorAll('.required-field');

                requiredFields.forEach(function (label) {
                    const inputId = label.getAttribute('for');
                    const input = document.getElementById(inputId);

                    if (input && !input.value.trim()) {
                        isValid = false;
                        input.classList.add('is-invalid');

                        // Créer un message d'erreur
                        if (!input.nextElementSibling || !input.nextElementSibling.classList.contains('invalid-feedback')) {
                            const errorDiv = document.createElement('div');
                            errorDiv.className = 'invalid-feedback';
                            errorDiv.textContent = 'Ce champ est obligatoire';
                            input.parentNode.appendChild(errorDiv);
                        }
                    } else if (input) {
                        input.classList.remove('is-invalid');
                        input.classList.add('is-valid');
                    }
                });

                if (!isValid) {
                    event.preventDefault();
                    alert('Veuillez remplir tous les champs obligatoires');
                }
            });
        });