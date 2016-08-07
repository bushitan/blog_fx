function Circle(x, y, radius, color) {
  this.x = x;
  this.y = y;
  this.radius = radius;
  this.color = color;
  this.isSelected = false;
}


ActiveCircle = {
  circles : [],
  canvas : null,
  context : null,

  Init:function(canvas_id)
  {
      this.canvas = document.getElementById(canvas_id);
      this.context = this.canvas.getContext("2d");

      //this.canvas.onmousedown = this.Click;

      this.Add = this.Add.after(this.Draw);
      this.Clear = this.Clear.after(this.Draw);
      this.Click = this.Click.after(this.Draw);
      //this.canvas.onmouseup = stopDragging;//鼠标松开，停止拖动
      //this.canvas.onmouseout = stopDragging;
      //this.canvas.onmousemove = dragCircle;
  },

  //增加圆圈
  Add:function(circle_data_arr)
  {
    for (var i=0;i<circle_data_arr.length;i++)
    {
      var circle = new Circle(
          circle_data_arr[i].x,
          circle_data_arr[i].y,
          circle_data_arr[i].radius,
          circle_data_arr[i].color);
      this.circles.push(circle);    // 保存到数组.
    }
  },

  //清空画布
  Clear:function() {
    this.circles = [];
  },

  //更新屏幕
  Draw:function()
  {
    //console.log('in draw');
    this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);

    for (var i = 0; i < this.circles.length; i++)
    {
      var circle = this.circles[i];
      this.context.globalAlpha = 0.85;
      this.context.beginPath();
      this.context.arc(circle.x, circle.y, circle.radius, 0, Math.PI * 2);
      this.context.fillStyle = circle.color;
      this.context.strokeStyle = "black";

      if (circle.isSelected) {
        this.context.lineWidth = 5;
      }
      else {
        this.context.lineWidth = 1;
      }
      this.context.fill();
      this.context.stroke();
    }
  },

  previousSelectedCircle:null,//记录前一个选中的圆

  firstSelectCircle : null,
  secondSelectCircle : null,

  //点击屏幕
  Click:function(clickX,clickY)
  {
    //console.log('in Click');

    // 判断点击了哪个圆.
    for (var i = this.circles.length - 1; i >= 0; i--) {
      var circle = this.circles[i];
      console.log(circle);
      console.log(circle.x);
      //console.log(circle+ ':'+circle.x+':'+circle.y);
      var distanceFromCenter = Math.sqrt(Math.pow(circle.x - clickX, 2) + Math.pow(circle.y - clickY, 2));
      if (distanceFromCenter <= circle.radius) {
        if (this.previousSelectedCircle != null) this.previousSelectedCircle.isSelected = false;
        this.previousSelectedCircle = circle;//记录选中的圆

        //第一次选中圆圈
        if (this.firstSelectCircle == null) {
          this.firstSelectCircle = circle;
          circle.isSelected = true;
          return ;
        }
        //第二次选中圆圈
        else if (this.secondSelectCircle == null) {
          //避免同一个圆选两次
          if (this.firstSelectCircle == circle)
          {
              circle.isSelected = true;
              return;
          }

          this.secondSelectCircle = circle;

          //两个圆圈颜色相同，消除
          if (this.firstSelectCircle.color == this.secondSelectCircle.color) {
            //删除第一个圆
            firstIndex = QueryIndex(this.circles, this.firstSelectCircle);
            this.circles.splice(firstIndex, 1);
            //删除第二个圆
            secondIndex = QueryIndex(this.circles, this.secondSelectCircle);
            this.circles.splice(secondIndex, 1);
          }

          //选择两次圆后，选择状态重置
          this.firstSelectCircle = null;
          this.secondSelectCircle = null;

        }
        //return ;
      }
    }
    //查询圆在数组中位置
    function QueryIndex(arr,element)
    {
      for (var i=0;i<arr.length;i++)
        if(arr[i] == element)
          return i;
    }

    if (this.circles.length == 0)
          GameOver()
  }


};

//页面初始化
var ac ;
var Load = function() {
  ac = ActiveCircle;
  ac.Init("canvas");

  document.getElementById('canvas').addEventListener("click", canvas_click);
  document.getElementById('clear').addEventListener("click", canvas_clear);
  function canvas_click(e)
  {
    var clickX = e.pageX - this.offsetLeft;
    var clickY = e.pageY - this.offsetTop;
    ac.Click(clickX,clickY);
  }
  function canvas_clear()
  {
    ac.Clear()
  }

  //Todo post获取数据

  circle_data_arr =[
      //{x: 84, y: 117, radius: 57, color: "#456ab6", isSelected: false},
      {x: 122, y: 151, radius: 54, color: "green", isSelected: false},
      {x: 44, y: 99, radius: 37, color: "green", isSelected: false}
  ];
  ac.Add(circle_data_arr)
};


Function.prototype.before = function( func ) {
   var __self = this;
   return function() {
          if ( func.apply( this, arguments ) === false ) {
                return false;
          }
       return __self.apply( this, arguments );
   }
};

Function.prototype.after = function( func ) {
   	var __self = this;
	   return function() {
		      var ret = __self.apply( this, arguments );
		      if( ret === false) {
			         return false;
		      }
		      func.apply( this, arguments );
		      return ret;
	   }
};

function randomFromTo(from, to) {
  return Math.floor(Math.random() * (to - from + 1) + from);
}
