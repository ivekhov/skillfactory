advice_url = "https://api.adviceslip.com/advice";


$("#main_header").click(function() {

	$.getJSON(advice_url, function(data) {

		advice = data["slip"]["advice"];
		set_secret_message(advice);

	});

});

function set_secret_message(msg) {

	    p = $('#second_paragraph');
		p.html(msg);
		p.css('color', 'red');

}





// $("#main_header").click(function() {

//         console.log("1: inside anonym function")

//         // $('#second_paragraph').html("secret message")

//         p = $('#second_paragraph');
// 		p.html("secret message");
// 		p.css('color', 'red');

// 		console.log("2: after styling");        	

// });