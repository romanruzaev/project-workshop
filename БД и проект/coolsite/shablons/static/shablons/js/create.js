const fileUploader = document.getElementById('document');//неизменяемая переменная, которая хранит веб-страницу??? со свойством возврата ссылки на элемент по id (https://developer.mozilla.org/ru/docs/Web/API/Document/getElementById)
const button = document.querySelector('#check__btn');//неизменяемая переменная, которая хранит веб-страницу со свойством возврата первого элемента в документе с идентичной меткой (https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)

fileUploader.addEventListener('change', (event) => {//обработчик события (стрелочная функция), 1 параметр - тип события (здесь: html тег <input> для выбора файла из проводника), 2 параметр - куда передает (слушатель)
    const files = event.target.files;//неизменяемая переменная, которая хранит файлы

    if (fileUploader.value.split('.').pop() != 'docx'){//у загружаемого файла рассматривается название, ставится разграничитель по точке, выводится расширение, которое сравнивается с docx
        alert('Выберите файл c расширением "docx"!')  
        var mess = ''
        const feedback = document.getElementById('feedback');//неизменяемая переменная, которая хранит веб-страницу??? со свойством возврата ссылки на элемент по id
        const msg = `${mess}`;//неизменяемая переменная, которая хранит
        feedback.innerHTML = mess;
        //alert(msg)
    }
});

button.addEventListener('click', function() {
    if (fileUploader.value == "")
        alert('Выберите файл!')
    else if (fileUploader.value.split('.').pop() == 'docx') {
        
        //------------------------------------
        var mess = 'Ошибок нет!'
        //------------------------------------

        const feedback = document.getElementById('feedback');
        const msg = `${mess}`;
        feedback.innerHTML = mess;
    }
});