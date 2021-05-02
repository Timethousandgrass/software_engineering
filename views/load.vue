<template>
  <div>
    <!--文件上传表单-->
    <form id="FF">
      <div>
        <div>
          <input type="text" name='Account' value="20180000" v-model="account" placeholder="请输入学号">
        </div>
        <div>
          <input type="text" name='password' value="" v-model="password" placeholder="请输入密码">
        </div>
        <div>
          <button @click="submit($event)">登录</button>
        </div>  
      </div>
      <div>
        <img src="../images/grass1.jpg">
      </div>
      
    </form>



    <p>
      {{mess}}
    </p>
  </div>
</template>

<script>
import axis from 'axios';

export default {
  data () {
    return{
      //文件
      account:'',
      password:'',
      mess:''
    }
  },
  methods:{
    submit(event) {
      event.preventDefault();//取消默认行为
      //创建 formData 对象

      const form = document.querySelector("#FF");
      const formData = new FormData();
      // 向 formData 对象中添加文件
      formData.append('account', this.account)
      formData.append('password', this.password)
      console.log(formData.get('account'))
      const config = {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      axis.post('/login/', formData, config).then(res=>{
        console.log("res: ", res);
        this.mess=res.data['right'];
        if (this.mess==='1') {
          console.log('here');
          window.localStorage.setItem('loaded',true)
          window.localStorage.setItem('account',this.account)
          window.localStorage.setItem('admin',res.data['admin'])
          this.$router.push('/choose')
        }else{
          console.log('biao')
        }
      });

    }
  }
}
</script>

<style scoped>

</style>