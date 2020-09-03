<template>
    <div>
        <div>
             <h1 class="ti">   Edit Note </h1>
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
         
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Body:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="note.body"
          required
        ></b-form-input>
      </b-form-group>

     

      <b-button  v-on:click="editNote" variant="primary"> Edit </b-button>
      <b-button  v-on:click="deleteNote" variant="danger"> Delete </b-button>
    </b-form>
   
     </b-container>
      </div>
    </div>
</template>


<script>
 import axios from 'axios';
 import { mapGetters } from 'vuex';

 export default{

   data() {
      return {
        id : this.$route.params.id,
        note:{  
          title: '',
          body: '',
         }, 
  
        show: true
      }
    },

    mounted(){
      axios
        .get('http://127.0.0.1:8000/api/v1/notes/'+ this.id,
           {headers: {'Authorization': 'JWT ' + this.loggedUser.token}} )
        
        .then( response => {
           this.note = response.data
        })
         .catch((err) => {
           console.log(err.response.data);
           });
     }, 

    computed:{
      ...mapGetters([
        'loggedUser'
      ])
     },

    methods:{
        
      editNote() {
         axios
         .put('http://127.0.0.1:8000/api/v1/notes/'+ this.id+'/',{
             title: this.note.title,
             body:  this.note.body,
             user:  this.loggedUser.user.pk
           },
            {headers: {'Authorization': 'JWT ' + this.loggedUser.token}}  
           )
         .catch((err) => {
           console.log(err.response.data);
           });

         this.$router.push('/notes')
    },
      
    deleteNote() {
      axios
        .delete('http://127.0.0.1:8000/api/v1/notes/'+ this.id +'/',
          {headers: {'Authorization': 'JWT ' + this.loggedUser.token}}
         )   
        .catch((err) => {
           console.log(err.response.data);
           });
        this.$router.push('/notes')
    },

  },  
}
   

</script>

<style scoped>
  
 .ti{

  color: lightblue;
  text-align: center;

}


</style>

 