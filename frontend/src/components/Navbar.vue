<template>
  <div>
   <b-nav class="fixed-top" align="center">

     <b-button v-b-popover.hover.top="'Login to write a note'" title="Login">
      New Note
    </b-button>
  
    <b-nav-item :to="{name: 'register'}">Register</b-nav-item>

    <b-nav-item-dropdown
      id="my-nav-dropdown"
      text="User"
      toggle-class="nav-link-custom"
      right
    >
      <b-dropdown-item :to="{name: 'login'}">  Login   </b-dropdown-item>
      <b-dropdown-item @click="logout()">  Logout  </b-dropdown-item>

       </b-nav-item-dropdown>

  </b-nav>

  
  </div>
  
</template>

<script>
  import axios from 'axios';
 
  export default{

 methods: {

  logout(){
      axios
        .post('http://127.0.0.1:8000/api/v1/rest-auth/logout/')
    },
  },

}
</script>