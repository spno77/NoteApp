<template>
    <div>
     
        <div>
             <h1 class="ti">  Register User </h1>
         <b-container>  
          <b-form  v-if="show">
      <b-form-group id="input-group-1" label="Username:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="user.username"
          required
          placeholder="Enter Username"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Email:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="user.email"
          type="email"
          required
          placeholder="Enter Email"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="user.password1"
          type="password"
          required
          placeholder="Enter password"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Password:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="user.password2"
          type="password"
          required
          placeholder="Re-enter password"
        ></b-form-input>
      </b-form-group>


      <b-button  v-on:click="onSubmit" variant="primary"> Register </b-button>
    </b-form>
   
     </b-container>
      </div>
    </div>
</template>


<script>
 import axios from 'axios';

  export default {
    data() {
      return {    
      
      user:{  
        username: '',
        email: '',
        password1: '',
        password2: '',
       
       } ,
        
        show: true
      }
    },

    methods: {

      onSubmit() {
        axios
          .post('http://127.0.0.1:8000/api/v1/rest-auth/registration/',{

             username:   this.user.username,
             email:      this.user.email,
             password1:  this.user.password1,
             password2:  this.user.password2,
          })
      },
    }
  }
</script>


<style scoped>
  
.ti{

  color: lightblue;
  text-align: center;

}

</style>