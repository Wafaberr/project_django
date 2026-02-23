const table_rows = document.querySelectorAll('tbody tr'),
      table_headings_all = document.querySelectorAll('thead th');

let table_headings = Array.from(table_headings_all).slice(0, -1);

table_headings.forEach((head, i) => {
    let sort_asc = true;
    head.onclick = () => {
        try {
            // Supprimer tous les active
            table_headings.forEach(head => head.classList.remove('active'));
            head.classList.add('active');

            document.querySelectorAll('td').forEach(td => td.classList.remove('active'));
            
            // Vérifier que la colonne existe pour chaque ligne
            table_rows.forEach(row => {
                const cells = row.querySelectorAll('td');
                if (cells[i]) {
                    cells[i].classList.add('active');
                }
            });

            head.classList.toggle('asc', sort_asc);
            sort_asc = head.classList.contains('asc') ? false : true;   

            sortTable(i, sort_asc);
        } catch (error) {
            console.error('Erreur lors du tri:', error);
        }
    };
});

function sortTable(column, sort_asc) {
    try {
        const rowsArray = Array.from(table_rows);
        
        rowsArray.sort((a, b) => {
            const aCells = a.querySelectorAll('td');
            const bCells = b.querySelectorAll('td');
            
            // Vérification de sécurité
            if (!aCells[column] || !bCells[column]) {
                console.warn(`Colonne ${column} manquante dans une ligne`);
                return 0;
            }
            
            let valueA = aCells[column].textContent.toLowerCase().trim();
            let valueB = bCells[column].textContent.toLowerCase().trim();
            
            // Détection automatique du type (nombre ou texte)
            if (!isNaN(valueA) && !isNaN(valueB) && valueA !== '' && valueB !== '') {
                // Tri numérique
                return sort_asc ? 
                    parseFloat(valueA) - parseFloat(valueB) : 
                    parseFloat(valueB) - parseFloat(valueA);
            } else {
                // Tri alphabétique
                if (sort_asc) {
                    return valueA.localeCompare(valueB);
                } else {
                    return valueB.localeCompare(valueA);
                }
            }
        });
        
        // Réorganiser le tableau
        const tbody = document.querySelector('tbody');
        rowsArray.forEach(row => tbody.appendChild(row));
        
    } catch (error) {
        console.error('Erreur dans sortTable:', error);
    }
}

const searchInput = document.querySelector('.input-group input');

searchInput.addEventListener('input',searcheTable);

function searcheTable() {
    table_rows.forEach((row, i) => {
        let rowText = row.textContent.toLowerCase(),
            searchText = searchInput.value;
        
            rowText.indexOf(searchText) > -1 ? row.style.display = '' : row.style.display = 'none';
        
    });
}