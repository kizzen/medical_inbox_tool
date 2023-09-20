$(document).ready(function() {
    $('#generateResponseBtn').click(function() {
        // Grey out the button and prevent further clicks
        $(this).prop('disabled', true).css('background-color', '#a8a5a5').css('cursor', 'not-allowed');

        $.ajax({
            url: '/get_answers',
            method: 'POST',
            dataType: 'json',
            data: { index: $('#currentIndex').val() },  // sending index value
            success: function(data) {
                $('.response-box:eq(0)').text(data.answers_nc);
                $('.response-box:eq(1)').text(data.answers_wc);
            },
            error: function() {
                alert("An error occurred while fetching responses.");
            }
        });
    });
});