getviewUrl="/baidu/get_comment";

compareUrl="/baidu/get_similarity";

spiteword_baiduUrl="/baidu/get_split";

function getView(text,typenum){
	$.getJSON(getviewUrl,function(result){
		if(result.message=="获取成功")
			localStorage.setItem("keywords",JSON.stringify(result.data));
	})
}
