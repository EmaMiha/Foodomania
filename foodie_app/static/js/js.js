document.addEventListener('DOMContentLoaded', () => {

    const container = document.getElementById('ingredients-container');
    const container2 = document.getElementById('instructions-container');
    container.addEventListener('keydown', (event) => {
        if (event.target.classList.contains('ingredient-input') && event.key === 'Enter') {
            event.preventDefault();
            const newInput = document.createElement('input');
            newInput.type = 'text';
            newInput.name = 'ingredients[]';
            newInput.className = 'ingredient-input';
            newInput.placeholder = 'Enter an ingredient';
            container.appendChild(newInput);
            newInput.focus();
        }
    });   
    
    container2.addEventListener('keydown', (event) => {
        if (event.target.classList.contains('instruction-input') && event.key === 'Enter') {
            event.preventDefault();
            const newInput = document.createElement('input');
            newInput.type = 'text';
            newInput.name = 'instructions[]';
            newInput.className = 'instruction-input';
            newInput.placeholder = 'Enter an instruction';
            container2.appendChild(newInput);
            newInput.focus();
        }
    });
});