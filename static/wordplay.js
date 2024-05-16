$(document).ready(function() {

    var items1 = ["softer", "stoneware", "software", "solitaire", "sportswear"],
        $text = $( '#wordplay1' ),
        delay = 2; //seconds

    var items2 = ["enveloper", "teleprompter", "developer", "thunderflower", "helicopter"],
        $text2 = $( '#wordplay2' );
    
        
    function loop1 ( delay ) {
        $.each( items1, function ( i, elm ){
            $text.delay( delay*1E3).fadeOut();
            $text.queue(function(){
                    $text.html( items1[i] );
                    $text.dequeue();
                });
            $text.fadeIn();
            $text.delay( delay*1E3);
            $text.queue(function(){
                if ( i == items1.length -1 ) {
                    loop1(delay);   
                }
                $text.dequeue();
            });
        });
    }

    function loop2 ( delay ) {
        $.each( items2, function ( i, elm ){
            $text2.delay( delay*1E3).fadeOut();
            $text2.queue(function(){
                $text2.html( items2[i] );
                $text2.dequeue();
            });
            $text2.fadeIn();
            $text2.delay( delay*1E3);
            $text2.queue(function(){
                if ( i == items2.length -1 ) {
                    loop2(delay);   
                }
                $text2.dequeue();
            });
        });
    }

    const wait = (ms) => new Promise(resolve => setTimeout(resolve, ms))

    const play = async () => {
        loop1( delay );
        await wait(3000);
        loop2( delay );
    }

    play();
    
});