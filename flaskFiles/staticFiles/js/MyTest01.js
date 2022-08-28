
function clickMe() {
    let result = "Hello world!";
    showTitleInDiv(result);
    return result;
}

function showTitleInDiv(val) {
    $("#div1").text(val);
}

function get_suggest() {
	var kw = document.getElementById('search_input').value;
	var clear = document.getElementById('clear');
	if (kw) clear.style.display = 'block';
	else clear.style.display = 'none';
	if (kw == last_kw) return;
	last_kw = kw;
	if (!kw || kw.length < max_sug_len) {
		close_sug();
		return;
	}
	var script = document.createElement('script');
	script.type = 'text/javascript';
	script.src = 'http://sugs.m.sm.cn/web?t=w&uc_param_str=dnnwnt&scheme=http&fr=android&bid=1&q=' + encodeURIComponent(kw) + '&_=' + new Date().getTime() + '&callback=jsonp3';
	var head = document.querySelector('head');
	script.onload = function() {
      head.removeChild(script);
	};
	head.appendChild(script);
}

function jsonp3(res) {
	var suggest = document.getElementById('suggest');
	if (!res.r || !res.r.length) {
		suggest.style.display = 'none';
		return;
	}
	var html = '';
	res.r.forEach(function(v) {
		html += '<li>' + v.w + '<b></b></li>';
	});
	document.getElementById('suglist').innerHTML = html;
	suggest.style.display = 'block';
}

function close_sug() {
	last_kw = '';
	document.getElementById('suggest').style.display = 'none';
}

function move_input() {
	document.body.scrollTop = document.getElementById('search_form').offsetTop - 2;
}

function clear_seach() {
	var input = document.getElementById('search_input');
	input.value = '';
	document.getElementById('clear').style.display = 'none';
	close_sug();
	input.focus();
}

function search(){
    if(document.getElementById("search_input").value != ""){
        window.location.href = "http://m.sm.cn/s?q=" + encodeURIComponent(document.getElementById("search_input").value) + "&from=smor&safe=1&snum=1";
        document.getElementById("search_input").value = "";
    }
    return false;
}