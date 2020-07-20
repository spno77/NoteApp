<template>
  <div>
   <b-nav align="center">

    <b-nav-item :to="{name: 'register'}">Register</b-nav-item>

    <b-nav-item-dropdown
      id="my-nav-dropdown"
      text="User"
      toggle-class="nav-link-custom"
      right
    >
      <b-dropdown-item>  Login   </b-dropdown-item>
      <b-dropdown-item>  Logout  </b-dropdown-item>

       </b-nav-item-dropdown>

  </b-nav>

  <div class="center my-3">
    <b-button v-b-popover.hover.top="'Login to write a note'" title="Login">
      New Note
    </b-button>
  </div>
  
  </div>
  
</template>

