var changer = 'frog1';

function change()
{
    var image = document.getElementById('frog1');

    if(changer == 'frog1')
    {
        image.style.height = '400px';
        image.style.width = '500px';
        image.src = 'https://pbs.twimg.com/profile_images/1243926376803172353/-dkX7Bwc_400x400.jpg';
        changer = 'frog2';
    }
    else
    {
        image.src = 'https://www.zsl.org/sites/default/files/image/2014-02/mountainchickenfrog.jpg';
        changer = 'frog1';
    }
}