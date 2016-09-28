DrawingBoard.Control.Download = DrawingBoard.Control.extend({

	name: 'download',

	initialize: function() {
		this.$el.append('<button class="drawing-board-control-download-button"></button>');
		this.$el.on('click', '.drawing-board-control-download-button', $.proxy(function(e) {
			//this.board.downloadImg();
			//e.preventDefault();
			//var draw_img = this.board.getImg();
			var canvas = $(".drawing-board-canvas")[0];

			//draw_img = img.replace("image/png", "image/octet-stream");
			//console.log(draw_img)

			 $.ajax({
					type: "POST",
					url: '/blog/board/',
					data:{
						"bg_img": "bg.jpg",
						"draw_img": canvas.toDataURL().split(',')[1],
						"gif_sprite_img":"test"
						//"artwork_index":artwork_index
					},
					success:function(data,textStatus){
						alert("头像上传完毕！")
					},
					error:function(XMLHttpRequest, textStatus, errorThrown){
						alert(XMLHttpRequest.responseText);
					}
			 });

		}, this));
	}

});