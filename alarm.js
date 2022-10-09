
function time(){
    let now = new Date();
    let h = now.getHours() + 1;
    let m = now.getMinutes();
    let s = now.getSeconds();
    let real_time = `${h}:${m}:${s}`;
    document.getElementById('clock').innerHTML = `${real_time}`;
}

setInterval(time, 1000);

// function setAlarm(hour, minute){
//     let now = new Date();
//     let minutes = now.getMinutes();
//     let hours = now.getHours();
//     let alarm_h;
//     let alarm_m;
//     if(hour >= hours && minute >= minutes){
//         alarm_h = hour - hours;
//         alarm_m = minute - minutes;
//     }
//     else if(hour >= hours && minute < minutes){
//         alarm_h = hour - hours - 1;
//         alarm_m = 60 - minutes + minute;
//     }
//     else if(hour < hours && minute >= minutes){
//         alarm_h = 23 - hours + hour;s
//         alarm_m = minute - minutes;
//     }
//     else if(hour < hours && minute < minutes){
//         alarm_h = 23 - hours + hour;
//         alarm_m = 60 - minutes + minute;
//     }
//     console.log(`time is ${alarm_h}h${alarm_m}m`);
//     let time = alarm_h * 3600000 + alarm_m * 60000;
//     setTimeout(ring, time);
// }

// function ring(){
//     document.getElementById('clock').innerHTML = 'Time to get up!';
// }

// // stop alarm
// document.getElementById('upBtn').onclick = function(){
//     console.log("I'm up.");
// }

// // snooze
// document.getElementById('snoozeBtn').onclick = function(){
//     console.log("I'm getting a snooze.");
//     let snooze_time = 1;
//     setTimeout(() => alert('TIME TO GET UP'), snooze_time*60000);
// }

// setAlarm(17, 36);


// function countTime(){
//     let now = new Date();
//     let h = now.getHours() + 1;
//     let m = now.getMinutes();
//     let s = now.getSeconds();
// }



