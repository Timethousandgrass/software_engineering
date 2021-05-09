<template>
  <!--文件上传表单-->
  <form id="FF">
    <a @click="GotoMine()">我的订单</a>
    <a @click="GotoLoad()">重新登陆</a>
    <div>
      <input type="text" name='key' value="" v-model="what" placeholder="请输入名字">
      <button @click="submit($event)">查询</button>
    </div>
    <div v-for="item in li">
      <p>车辆编号{{item['no']}}</p>
      <p>车辆类型:{{item['name']}}</p>
      <p>车辆使用年龄:{{item['age']}}</p>
      <p>车辆价格:{{item['money']}}</p>
      <img  v-for="pic in item['pics']" @click="Goto(item)" :src=pic height="100px">
    </div>
  </form>
</template>

<script>
import axis from 'axios';

export default {
  // name: "submit",
  data () {
    return{
      what:'山地车',

      li:[]
    }
  },
  methods:{
    getFile(event) {
      this.file = event.target.files[0];
      console.log(this.file);
    },
    GotoMine(){
      this.$router.push('/mine')
    },
    GotoLoad(){
      this.$router.push('/load')
    },
    submit(event) {
      event.preventDefault();//取消默认行为
      //创建 formData 对象
      this.li=[]
      const form=document.querySelector("#FF");
      const formData = new FormData();
      // 向 formData 对象中添加文件
      formData.append('key',this.what)
      // console.log(this.name)
      console.log(formData.get('key'))
      const config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axis.post('/search/', formData, config).then(res=>{
        console.log(res.data);
        this.li=res.data;
        console.log(this.li)
        console.log(this.li[0])
      });
    },
    Goto(item){
      this.$router.push({name:'single',params:item})
    }
  }
}
</script>

<style scoped>

</style>