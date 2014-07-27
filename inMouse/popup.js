offset=25;
arr = [];


function mrd(event)
{
	
	var x = event.clientX;
	var y = event.clientY;
	for(var i = 0; i<arr.length; i++)
	{
		if(arr[i].offset().top - offset > y) continue;
		else if (arr[i].offset().top + arr[i].height() + offset < y) continue;
		else if (arr[i].offset().left - offset > x) continue;
		else if (arr[i].offset().left + arr[i].width() + offset < x) continue;
		else
		{
			arr[i].focus();
			console.log("Thgis isa sdfa");
		}
		
	}
}





$(document).ready(function(){




//$("body").attr("onmousemove","mrd(event)");
document.addEventListener("mousemove",mrd)

$("a").each(function() {
    var link = $(this);
    var top = link.offset().top;
    var left = link.offset().left;
    var width = link.offset().width;
    var height = link.offset().height;
	
	arr.push(link);
});


$("button").each(function() {
    var link = $(this);
    var top = link.offset().top;
    var left = link.offset().left;
    var width = link.offset().width;
    var height = link.offset().height;
	arr.push(link);
	
});

});
