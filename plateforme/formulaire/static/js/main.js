 
 
 
 
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
 
 
 

 
 
 
