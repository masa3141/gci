//ランダムデータセット生成
// var dataSet = d3.range(180).map(function() {
//     return {
//       '年齢': 19 + ~~(Math.random() * 30),
//       '家族':  ~~(Math.random() * 2) + ~~(Math.random() * 2)+ ~~(Math.random() * 3),
//       '身長':160 +  ~~(Math.random() * 30),
//       '体重':40 + ~~(Math.random() * 50),
//       'BMI(％)': 7 + ~~(Math.random() * 10) + ~~(Math.random() * 10)+ ~~(Math.random() * 10)+ ~~(Math.random() * 10),
//       '年収(万円)':300 +  ~~(Math.random() * 600)
//       };
// });

d3.tsv('data/twitter.tsv', function(data) {


  var dataSet = data;

//パラレルコーディネート用ステージ
var example = d3.select('#example')
    .style({
    "width":"1500px",
    "height":"650px",
    });


// カラースケール
var blue_to_brown = d3.scale.linear()
    .domain([300, 799,800, 900])
    .range(['blue', 'blue', 'red', 'red'])
    .interpolate(d3.interpolateLab);

//パラレルコーディネート生成
var pc = d3.parcoords()('#example')
    .data(dataSet)
//    .color(function(d) { return blue_to_brown(d['年収(万円)']); })
    .alpha(0.4)
    .composite('lighter')
    .render()
    .ticks(5)
    .createAxes()
    .brushable(); //絞り込み可能にする


//データテーブル作成
var grid = d3.divgrid();
d3.select('#grid')
  .datum(dataSet.slice(0,300)) //表示件数の指定
  .call(grid)
  .selectAll('.row')
  .on({
      'mouseover': function(d) { pc.highlight([d]) },
      'mouseout': pc.unhighlight
  });


// データテーブルの更新
pc.on('brush', function(d) {
  d3.select('#grid')
    .datum(d.slice(0,300))
    .call(grid)
    .selectAll('.row')
    .on({
    'mouseover': function(d) { pc.highlight([d]) },
    'mouseout': pc.unhighlight
    });
});

});

