<template>
  <div>
   <b-nav class="fixed-top" align="center">

    <b-nav-item :to="{name: 'notes'}"> Home </b-nav-item>
   
     <b-button :to="{name: 'create'}" v-b-popover.hover.top="'Login to write a note'" title="Login">
      New Note
    </b-button>
  

    <b-nav-item-dropdown
      id="my-nav-dropdown"
      text="User"
      toggle-class="nav-link-custom"
      right
    >
      <b-dropdown-item v-if="isLoggedIn===false" :to="{name: 'register'}">  Register  </b-dropdown-item>
      <b-dropdown-item v-if="isLoggedIn===false" :to="{name: 'login'}">  Login   </b-dropdown-item>

      <b-dropdown-item v-if="isLoggedIn===true" @click="logoutUser">  Logout  </b-dropdown-item>

       </b-nav-item-dropdown>

  </b-nav>

  
  </div>
  
</template>

<script>
  //import axios from 'axios';
  import { mapActions } from 'vuex';
  import { mapGetters } from 'vuex';
 
  export default{

  methods: {

  ...mapActions(['logoutUser']),
  },

  computed:{
      ...mapGetters([
        'loggedUser',
        'isLoggedIn',
      ])
     },

}
</script>