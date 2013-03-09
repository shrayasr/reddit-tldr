$(function(){

	$("#how-many").focus();

	$("#loading-bar").hide();

	$(document).ajaxStart(function(){
		$("#loading-bar").show();
	}).ajaxStop(function(){
		$("#loading-bar").hide();
	});
	
	$("#go-button").click(function(){

		var tldrs = $("#how-many").val();

		console.log("Fetching "+tldrs+" tldr's");

		$.getJSON('/tldr/tldrs/'+tldrs,function(json){

			$("#tldr-area").html("");

			$.each(json.data,function(key,value){

				var heading = value.heading.toString().toLowerCase();

				if (heading == "false"){

					var appender = '<li class="tldr-text"><a href="'+value.link+'" target="_blank">'+value.text+'</a></li>';
					$("#tldr-area").append(appender);

				}

				else{

					var appender = '<li class="tldr-heading">'+value.text+'</li>';
					$("#tldr-area").append(appender);

				}


			});

		});

	});

});
