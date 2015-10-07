$(document).ready(function(){

	$("#reload").click( function() {
		location.reload();
	});

	$(".list-group-item").mouseover( function() {
		$(this).css("background-color", "#d3d3d3");
	});

	$(".list-group-item").mouseleave( function() {
		$(".list-group-item").css("background-color", "#ffffff");
	});

	$(".list-group-item").click( function() {
		
		var id = $(this).children("span").attr("id");
				
		parameter = "parameter="+id;
		change_panels(parameter);
	});

	function get_data(parameter){

		$.ajax({
		  	url: 'http://localhost:8888/asset',
			type: 'POST',
			data: { parameter },
			dataType: 'html',
			success: function(data) {
				if( data != null ){
					data = JSON.parse(data);
					write_data(data);
					$(".hidden").removeClass("hidden");
				}
			}
		});
 		
 		return null;
	}

	function write_data( data ){
		change_dns(data["dns"]);
		change_whois(data["whois"]);
		change_banner(data["banner"], data["screenshot"]);
		change_domain_name(data["domainName"]);
	}

	function change_panels(parameter){

		var dns    = "data";
		var whois  = "whois";
		var banner = "banner";
		var data   = null;

		data = get_data(parameter);

	}

});

function change_domain_name(data){
	$("#domain_name").html(data);
}

function change_dns( data ){
	$("#dns_body").html(data);
}

function change_whois( data ){
	$("#whois_body").html(data);
}

function change_banner( content, screenshot ){
	$("#banner_body").html(content);

	if(screenshot != "" ){
		screenshot = screenshot.substring(2,screenshot.length-1);
		var imgTag = "<img src='data:image/png;base64,"+ screenshot +"' />";
		$("#banner_img").html(imgTag)
	}
}
