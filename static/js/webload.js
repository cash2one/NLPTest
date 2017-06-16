windowheight = $(window).height()
bodyheight = $("body").height()
if(windowheight > bodyheight)
	$("#container").css("height", windowheight + "px")
else
	$("#container").css("height", bodyheight + "px")

$("#compare").click(function() {
	location.href = "comparePage.html";
})

$("#baidu_btn").click(function() {
	location.href = "NLPPageBaidu.html"
})

$("#tencnt_btn").click(function() {
	location.href = "NLPPageTencent.html"
})

$("#Boson_btn").click(function() {
	location.href = "NLPPageBoson.html"
})

$("#getview_btn").click(function() {
	typeNum = $("#typeSelect").val()
	txt = $("#viewbox").val()
	//	$.getJSON(getviewUrl + "?text=" + txt + "&type=" + typeNum, function(result) {
	//		if(result.message == "获取成功" && result.data != "")
	//			var resulttxt = ""
	//		for(var i = 0; i < result.data.length; i++)
	//			resulttxt = resulttxt + result.data[i].abstract + "\n";
	//		$("#viewanswerbox").html(result.data[i].abstract)
	//	})
	data = {
		"text": txt,
		"type": typeNum
	}
	$.ajax({
		type: "post",
		url: getviewUrl,
		data: data,
		dataType: "Json",
		success: function(result) {
			var resulttxt = ""
			if(result.message == "获取成功" && result.data != "")
				for(var i = 0; i < result.data.length; i++) {
					abstract = "摘要：" + result.data[i].abstract;
					adj = "评价：" + result.data[i].adj;
					fea = "属性：" + result.data[i].fea;
					if(result.data[i].type == 2)
						type = "情感：积极";
					else if(result.data[i].type == 1)
						type = "情感：中性";
					else
						type = "情感：消极";
					resulttxt = resulttxt + abstract + "\n" + adj + "\n" + fea + "\n" + type + "\n\n";
				}
			else {
				resulttxt = "";
				alert("您输入的格式不在服务范围内，请重新输入")
			}

			$("#viewanswerbox").html(resulttxt)
		}
	});
})

$("#similarbtn").click(function() {
	txt1 = $("#txt1").val()
	txt2 = $("#txt2").val()
	data = {
		"text1": txt1,
		"text2": txt2
	}
	$.ajax({
		type: "post",
		url: compareUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var value = 0;
			if(result.message == "获取成功") {
				value = result.data.output.score;
			} else {
				value = 0
			}
			$("#percent").html((value * 100).toFixed(2) + "%");
			$("#progressfsimilar").attr("style", "width:" + (value * 100).toFixed(2) + "%;")
		}
	});

})

$("#keyword_tencent_btn").click(function() {
	txt1 = $("#txt1").val()
	data = {
		"title": txt1,
		"text": txt1
	}
	$.ajax({
		type: "post",
		url: getkeyWord_tencentUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var keywordresult = ""
			if(result.message == "获取成功") {
				for(var i = 0; i < result.data.length; i++) {
					str = eval("'" + result.data[i].keyword + "'")
					keywordresult = keywordresult + "关键词" + (i + 1) + ":" + str + "\n";
				}
			} else {
				keywordresult = "";
				alert("未取到关键词")
			}
			$("#txt2").html(keywordresult);
		}
	});

})

$("#classify_tencentbtn").click(function() {
	txt1 = $("#classifyinput").val()
	var data = {
		"text": txt1
	}
	$.ajax({
		type: "post",
		url: classify_tencentUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var classifyresult = ""
			if(result.message == "获取成功") {
				for(var i = 0; i < result.data.length; i++) {
					str = eval("'" + result.data[i].class + "'")
					conf = result.data[i].conf;
					classifyresult = classifyresult + "分类" + (i + 1) + ":" + str + "&nbsp&nbsp&nbsp&nbsp置信度：" + (conf * 100).toFixed(2) + "%" + "\n";
				}
			} else {
				classifyresult = "";
				alert("未取到分类文本")
			}
			$("#classifyoutput").html(classifyresult);
		}
	});

})

$("#EmotionBtn").click(function() {
	txt1 = $("#emotiontxt").val()
	var data = {
		"text": txt1
	}
	$.ajax({
		type: "post",
		url: emotion_tencentUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var positive = 0;
			var negative = 0;
			if(result.message == "获取成功") {
				positive = result.data.positive;
				negative = result.data.negative;
			}
			$("#positive").html("积极：" + parseInt(positive * 100) + "%");
			$("#negative").html("消极：" + parseInt(negative * 100) + "%");
			$("#progressfemotion_positive").attr("style", "width:" + parseInt(positive * 100) + "%;")
			$("#progressfemotion_negative").attr("style", "width:" + parseInt(negative * 100) + "%;")
		}
	});
})

$("#similarwordbtn").click(function() {
	txt1 = $("#similarwordtxt").val()
	var data = {
		"text": txt1
	}
	$.ajax({
		type: "post",
		url: similarword_tencentUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var similarwordresult = ""
			if(result.message == "获取成功") {
				for(var i = 0; i < result.data.length; i++) {
					similarwordresult = similarwordresult + result.data[i][0].word_ori + ":" + "\n";
					for(var l = 1; l < result.data[i].length; l++) {
						str = eval("'" + result.data[i][l].text + "'")
						conf = result.data[i][l].conf;
						similarwordresult = similarwordresult + "同义词" + l + ":" + str + "&nbsp&nbsp&nbsp&nbsp" + "置信度：" + (conf * 100).toFixed(2) + "%”" + "\n";
					}

				}
			} else {
				similarwordresult = "";
				alert("未获取到同义词")
			}
			$("#similarwordresulttxt").html(similarwordresult);
		}
	});
})

$("#correctwordbtn").click(function() {
	txt1 = $("#correctwordtxt").val()
	var data = {
		"text": txt1
	}
	$.ajax({
		type: "post",
		url: correctword_tencentUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var correctwordresult = ""
			if(result.message == "获取成功") {
				for(var i = 0; i < result.data.length; i++) {
					str = eval("'" + result.data[i].text + "'")
					conf = result.data[i].conf;
					correctwordresult = correctwordresult + "正确语句:" + str + "&nbsp&nbsp&nbsp&nbsp" + "置信度：" + (conf * 100).toFixed(2) + "%”" + "\n";
				}
			} else {
				correctwordresult = "";
				alert("未获取到纠错结果")
			}
			$("#correctwordresulttxt").html(correctwordresult);
		}
	});
})

$("#comparebtn").click(function() {
	var inputtxt = $("#inputtxt").val();
	var data = {
		"text": inputtxt
	}
	$.ajax({
		type: "post",
		url: spiteword_baiduUrl,
		data: data,
		dataType: "Json",
		success: function(result) {
			var baiduresult = ""
			if(result.message == "获取成功") {
				baiduresult = baiduresult + result.data.scw_out.wordsepbuf.trim();
			} else {
				baiduresult = "未获取到分词结果";
			}
			$("#baidutxt").html(baiduresult);
			$.ajax({
				type: "post",
				url: splitword_tencentUrl,
				data: data,
				dataType: "Json",
				success: function(result) {
					var tencentresult = ""
					if(result.message == "获取成功") {
						for(var i = 0; i < result.data[0].tokens.length; i++) {
							str = eval("'" + result.data[0].tokens[i].word + "'")
							tencentresult = tencentresult + str + "\t";
						}
					} else {
						tencentresult = "";
						alert("未获取到纠错结果")
					}
					$("#tencenttxt").html(tencentresult);
				}
			});
		}
	});
})

$("#BosonEmotionBtn").click(function() {
	var inputtxt = $("#BosonEmotiontxt").val();
	var data = {
		"text": inputtxt
	}
	$.ajax({
		type: "post",
		url: getEmotionUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var positive = 0;
			var negative = 0;
			if(result.message == "获取成功") {
				positive = result.data[0][0];
				negative = result.data[0][1];
			}
			$("#bosonpositive").html("积极：" + parseInt(positive * 100) + "%");
			$("#bosonnegative").html("消极：" + (100 - parseInt(positive * 100)) + "%");
			$("#Boson_progressfemotion_positive").attr("style", "width:" + parseInt(positive * 100) + "%;")
			$("#Boson_progressfemotion_negative").attr("style", "width:" + (100 - parseInt(positive * 100)) + "%;")
		}
	});
})

$("#keyword_boson_btn").click(function() {
	var inputtxt = $("#boson_keyword_input").val();
	var data = {
		"text": inputtxt
	}
	$.ajax({
		type: "post",
		url: getKeyWordUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var keywordresult = ""
			if(result.message == "获取成功") {
				for(var i = 0; i < result.data.length; i++) {
					str = eval("'" + result.data[i][1] + "'")
					conf = result.data[i][0]
					keywordresult = keywordresult + "关键词" + (i + 1) + ":" + str + "&nbsp&nbsp&nbsp&nbsp" + "置信度：" + (conf * 100).toFixed(2) + "%”" + "\n";
				}
			} else {
				keywordresult = "";
				alert("未取到关键词")
			}
			$("#boson_keyword_output").html(keywordresult);
		}
	});
})

$("#boson_similarwordbtn").click(function() {
	txt1 = $("#boson_similarwordtxt").val()
	var data = {
		"text": txt1
	}
	$.ajax({
		type: "post",
		url: getSimilarWordUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var similarwordresult = ""
			if(result.message == "获取成功") {
				for(var i = 0; i < result.data.length; i++) {
					str = eval("'" + result.data[i][1] + "'")
					str = str.slice(0, -2);
					conf = result.data[i][0];
					similarwordresult = similarwordresult + "同义词" + (i + 1) + ":" + str + "&nbsp&nbsp&nbsp&nbsp" + "置信度：" + (conf * 100).toFixed(2) + "%”" + "\n";
				}
			} else {
				similarwordresult = "";
				alert("未获取到同义词")
			}
			$("#boson_similarwordresulttxt").html(similarwordresult);
		}
	});
})

$("#classify_bosonbtn").click(function() {
	txt1 = $("#boson_classifyinput").val()
	var data = {
		"text": txt1
	}
	$.ajax({
		type: "post",
		url: getClassifyUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var classifyresult = ""
			if(result.message == "获取成功" && result.data != null) {
				str = eval("'" + result.data + "'")
				classifyresult = classifyresult + "分类" + ":" + str + "\n";
			} else {
				classifyresult = "";
				alert("未取到分类文本")
			}
			$("#boson_classifyoutput").html(classifyresult);
		}
	});

})

$("#entity_boson_btn").click(function() {
	var inputtxt = $("#boson_entity_input").val();
	var data = {
		"text": inputtxt
	}
	$.ajax({
		type: "post",
		url: GetEntityUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var keywordresult = ""
			if(result.message == "获取成功") {
				for(var i = 0; i < result.data.entity.length; i++) {
					str = eval("'" + result.data.word[result.data.entity[i][0]] + "'")
					type = eval("'" + result.data.entity[i][2] + "'")
					keywordresult = keywordresult + "命名实体" + (i + 1) + ":" + str + "&nbsp&nbsp&nbsp类型:" + type + "\n";
				}
			} else {
				keywordresult = "";
				alert("未取到关键词")
			}
			$("#boson_entity_output").html(keywordresult);
		}
	});
})

$("#abstract_boson_btn").click(function() {
	var inputtxt = $("#boson_abstract_input").val();
	var data = {
		"text": inputtxt
	}
	$.ajax({
		type: "post",
		url: getAbstractUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var keywordresult = ""
			if(result.message == "获取成功") {
				str = result.data;
				keywordresult = keywordresult + "摘要:" + str;
			} else {
				keywordresult = "";
				alert("未取到关键词")
			}
			$("#boson_abstract_output").html(keywordresult);
		}
	});
})

$("#entity_harbin_btn").click(function() {
	var inputtxt = $("#harbin_entity_input").val();
	var data = {
		"text": inputtxt
	}
	$.ajax({
		type: "post",
		url: GetHarbinEntityUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var keywordresult = ""
			if(result.message == "获取成功") {
				str = result.data
				a = 1
				b = 1
				strs = new Array();
				i = 0;
				while(a != -1 && b != -1) {
					a = str.indexOf("[");
					b = str.indexOf("]");
					if(a == -1 || b == -1)
						break;
					len = str.length;
					strs[i] = str.substring(a + 1, b)
					str = str.substring(b + 1, len)
					i++;
				}
				for(var l = 0; l < strs.length; l++)
					keywordresult = keywordresult + "命名实体" + (l + 1) + ":" + strs[l] + "\n";

			} else {
				keywordresult = "";
				alert("未取到关键词")
			}
			$("#harbin_entity_output").html(keywordresult);
		}
	});
})

$("#RoleMark_harbin_btn").click(function() {
	var inputtxt = $("#harbin_RoleMark_input").val();
	var data = {
		"text": inputtxt
	}
	$.ajax({
		type: "post",
		url: GetHarbinRoleMarkUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var keywordresult = ""
			if(result.message == "获取成功") {
				str = eval("'" + result.data + "'")
				keywordresult = keywordresult + "角色语义标注" + ":" + str + "\n";
			} else {
				keywordresult = "";
				alert("未取到角色标注信息")
			}
			$("#harbin_RoleMark_output").html(keywordresult);
		}
	});
})

$("#Denpendency_harbin_btn").click(function() {
	var inputtxt = $("#harbin_Denpendency_input").val();
	var data = {
		"text": inputtxt
	}
	$.ajax({
		type: "post",
		url: GetHarbinDenpendencyUrl,
		dataType: "Json",
		data: data,
		success: function(result) {
			var keywordresult = ""
			if(result.message == "获取成功") {
				str = result.data
				keywordresult = keywordresult + "语义依存分析" + ":" + str + "\n";
			} else {
				keywordresult = "";
				alert("未取到语义依存分析")
			}
			$("#harbin_Denpendency_output").html(keywordresult);
		}
	});
})