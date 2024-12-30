document.addEventListener('DOMContentLoaded', function () {


    const ingredientDiv = document.getElementById("ingredient-inputs");
    const instructionDiv = document.getElementById("instruction-inputs");
    const addIngredient = document.getElementById("add-ingredient-btn");
    const addInstruction = document.getElementById("add-instruction-btn");


    addIngredient.addEventListener("click", function () {


        const newInput = document.createElement('div');
        newInput.classList.add('ingredient-item');
        newInput.innerHTML = `<input type="text" name="ingredients[]" class="ingredient-input" placeholder="Enter an ingredient" required>
                         <button type="button" class="btn btn-danger remove-ingredient">Delete</button>`;
        ingredientDiv.appendChild(newInput);


    });

    ingredientDiv.addEventListener("click", function (e) {

        if (e.target.classList.contains("remove-ingredient")) {

            e.target.parentElement.remove();
        }

    });




    addInstruction.addEventListener("click", function () {


        const newInput = document.createElement('div');
        newInput.classList.add('instruction-item');
        newInput.innerHTML = `<input type="text" name="instructions[]" class="instruction-input" placeholder="Enter an instruction" required>
                         <button type="button" class="btn btn-danger remove-instruction">Delete</button>`;
        instructionDiv.appendChild(newInput);


    });

    instructionDiv.addEventListener("click", function (e) {

        if (e.target.classList.contains("remove-instruction")) {

            e.target.parentElement.remove();
        }

    });



});