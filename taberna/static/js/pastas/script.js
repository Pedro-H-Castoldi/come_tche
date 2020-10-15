function date_today() {
    let today = new Date;
    let date = document.querySelector('#datetime');
    let day = today.getDate();
    let max_day = day;
    let month = today.getMonth() + 1;
    let max_month = month;
    let max_year = today.getFullYear();
    let hours = today.getHours();
    let minutes = today.getMinutes();

    if(month < 10) {
        month = `0${month}`;
        if(parseInt(month) < 9) {
            max_month = `0${parseInt(month)+1}`;
        }
        else {
            max_month = parseInt(month) + 1;
        }
    }

    if(month == 12) {
        max_month = '01';
        max_year = today.getFullYear() + 1;
    }

    if(day < 10) {
        day = `0${day}`;
    }
    else if(max_month == '02' && day >= 28) {
        let year = today.getFullYear();
        if(year%4 == 0 && year%100 != 0 || year%400 == 0) {
            max_day = 29;
        }
        else {
            max_day = 28;
        }
    }
    else if( (day == 31 && max_month == '04') || (day == 31 && max_month == '06') || (day == 31 && max_month == '09') || (day == 31 && max_month == 11) ) {
        max_day = 30;
    }

    if(minutes + 20 < 60) {
        minutes = minutes + 20;
    }

    else {
        minutes = (minutes + 20) - 60;
        if(minutes < 10) {
            minutes = `0${minutes}`;
        }
    }
    
    date.min = `${today.getFullYear()}-${month}-${day}T${hours}:${minutes}`;
    date.value = `${today.getFullYear()}-${month}-${day}T${hours}:${minutes}`;
    date.max = `${max_year}-${max_month}-${max_day}T${hours}:${minutes}`;
}

date_today();