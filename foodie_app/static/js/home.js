$(document).ready(function () {


    $('.comment-count').on('click', function () {
        var commentsHtml = $(this).closest('.comments-section').find('.allcomm').html();
        $('#commentModal .modal-body').html(commentsHtml);
        var myModal = new bootstrap.Modal(document.getElementById('commentModal'), {});
        myModal.show();
    });


    $('.btn-heart').on('click', function () {

        const userIsAuthenticated = "{{ user.is_authenticated|yesno:'true,false' }}" === 'true';

        if (!userIsAuthenticated) {
            const toast = document.createElement('div');
            toast.className = 'toast align-items-center text-white bg-warning border-0 position-fixed bottom-0 end-0 m-4';
            toast.setAttribute('role', 'alert');
            toast.setAttribute('aria-live', 'assertive');
            toast.setAttribute('aria-atomic', 'true');
            toast.innerHTML = `<div class="d-flex"><div class="toast-body">You must be logged in to like a recipe.</div><button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button></div>`;
            document.body.appendChild(toast);
            new bootstrap.Toast(toast).show();
            setTimeout(() => toast.remove(), 4000);
            return;
        }


        var recipeId = $(this).data('recipe-id');
        var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
        var button = $(this);

        $.ajax({
            url: "{% url 'like_recipe' 0 %}".replace("0", recipeId),
            type: 'POST',
            data: {
                'csrfmiddlewaretoken': csrfToken
            },
            success: function (response) {
                $('#like-count-' + recipeId).text(response.likes_count);

                if (response.liked) {
                    button.text(`❤️ ${response.likes_count}`);
                } else {
                    button.text(`🤍 ${response.likes_count}`);
                }
            },
            error: function () {
                alert("An error occurred while processing your request.");
            }
        });
    });
});