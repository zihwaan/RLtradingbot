$(document).ready(function() {
    var eventSource;

    $('#hyperparameter-form').on('submit', function(e) {
        e.preventDefault();
        var formData = $(this).serialize();

        $.ajax({
            url: '/train',
            method: 'POST',
            data: formData,
            success: function(response) {
                // 학습이 시작되면 로그 스트리밍 시작
                startLogStreaming();
                // 결과 표시
                displayResults(response);
            },
            error: function(xhr, status, error) {
                console.error("Error:", error);
                $('#log-container').append("<p>Error: " + error + "</p>");
            }
        });
    });

    function startLogStreaming() {
        if (eventSource) {
            eventSource.close();
        }
        $('#log-container').empty();
        eventSource = new EventSource('/stream');
        eventSource.onmessage = function(e) {
            $('#log-container').append(e.data + "<br>");
            $('#log-container').scrollTop($('#log-container')[0].scrollHeight);
        };
    }

    function displayResults(data) {
        // 로그 컨테이너 업데이트
        var logContent = '';
        for (var key in data) {
            if (data.hasOwnProperty(key) && key !== 'image_url') {
                logContent += key + ': ' + data[key] + '<br>';
            }
        }
        $('#log-container').append(logContent);

        // 이미지 표시
        if (data.image_url) {
            $('#image-container').html('<img src="' + data.image_url + '" alt="학습 결과">');
        }
    }

    function updateImage() {
        var img = document.getElementById('result-image');
        if (img) {
            img.src = img.src.split('?')[0] + '?t=' + new Date().getTime();
        }
    }

    // 10초마다 이미지 업데이트
    setInterval(updateImage, 10000);
});