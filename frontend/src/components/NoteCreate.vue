<template>
    <div>
        <div>
             <h1 class="ti">   Create Note  </h1>
         <b-container>	
          <b-form  v-if="show">
      <b-form-group
        id="input-group-1"
        label="Title:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="note.title"
          required
          placeholder="Enter title"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Note Body:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="note.body"
          required
          placeholder="Enter description"
        ></b-form-input>
      </b-form-group>
     

   


      <b-button  v-on:click="onSubmit" variant="primary">Submit</b-button>
    </b-form>
   
     </b-container>
      </div>
    </div>
</template>


<script>
 import axios from 'axios';
 import { mapGetters } from 'vuex';

  export default {
    data() {
      return {
        
        note:{  
          title: '',
          body: '',
         }, 
  
        show: true
      }
    },
   
    computed:{
      ...mapGetters([
        'loggedUser'
      ])
     },

    methods:{
   
      onSubmit(){
        axios
         .post('http://127.0.0.1:8000/api/v1/notes/',{
             title: this.note.title,
             body:  this.note.body,
             user:  this.loggedUser.user.pk
           },
          {headers: {'Authorization': 'JWT ' + this.loggedUser.token}}  
           )
         .catch((err) => {
         //handle error
           console.log(err.response.data);
           });
         }

      }

}

 
</script>


<style scoped>
  
.ti{

  color: lightblue;
  text-align: center;

}

</style>






