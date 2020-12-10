/*Defines*/
function randomValue(min, max) {
    return Math.random() * (max - min) + min;
}
function playstages(number) {
    return document.getElementById(number).play();
}

/*Finctions*/
$(function(){
    $('.main').append('<a href="monsters.html"><div><img src="img/monsters_thumbnail.png"></div></a><a href="stages.html"><div><img src="img/stages_thumbnail.png"></div></a><a href="quests.html"><div><img src="img/quests_thumbnail.png"></div></a><a href="jobs.html"><div><img src="img/jobs_thumbnail.png"></div></a><a href="faq.html"><div><img src="img/faq_thumbnail.png"></div></a>');
    $('.saisyu_koshin').append('<br><span style="color: rgb(208, 234, 255);">最終更新日:2020/12/11</span>');
    $(".top_move").click(function () {
        $("html,body").animate({
            scrollTop:0
        },"300");
    });
});