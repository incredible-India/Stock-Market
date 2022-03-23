//checking the internet connection
if(!navigator.onLine)
{
    alert('Please on the internet connection')
}

function searchDATA(compName) {
    let extrctDATA ;
  extrctDATA= fetch(`https://api.polygon.io/v2/aggs/ticker/${compName}/range/1/day/2020-06-01/2020-06-17?apiKey=WUjrwnIGPdUHzQVEdnepsnY6LkEHYVbs`)
    .then((data) => data.json()).then(data=>{
      
 
    return data;

    }).catch((err) => {
        
        return {status:false, data:'Data could not be extracted please check your internet connection or symbol that you entered.'}
    })
  

    return {status : true,data : extrctDATA}
}

//showing the html data
function showResult(maindata) {

    if(mainData.resultsCount !=0)
    {
        document.getElementsByClassName('result')[0].innerHTML=''
        document.getElementsByClassName('result')[0].innerHTML = `<table class="table table-striped ">
        <thead>
          <tr>
            <th scope="col">Day</th>
            <th scope="col">trading volume </th>
            <th scope="col"> volume weighted average price</th>
            <th scope="col">open price</th>
            <th scope="col">close price</th>
            <th scope="col">highest price</th>
            <th scope="col">lowest price</th>
            <th scope="col">Unix Msec timestamp </th>
            <th scope="col">number of transactions</th>
          </tr>
        </thead>
        <tbody class='insert'>
        
        
        </tbody>
      </table>`

      document.getElementsByClassName('insert')[0].innerHTML =''
      
      for(i=0;i<mainData.resultsCount;i++){
     
        document.getElementsByClassName('insert')[0].innerHTML +=`

        <tr>
        <th scope="row">Day ${i+1}</th>
        <td>${mainData.results[i].v}</td>
        <td>${mainData.results[i].vw}</td>
        <td>${mainData.results[i].o}</td>
        <td>${mainData.results[i].c}</td>
        <td>${mainData.results[i].h}</td>
        <td>${mainData.results[i].l}</td>
        <td>${mainData.results[i].t}</td>
        <td>${mainData.results[i].n}</td>
    
      </tr>
        
        `
      }
    }else
    {
        document.getElementsByClassName('result')[0].innerHTML = `<div class='container mt-3 alert-info text-dark'> No data found !! Please check the company symbol or internet connection `
    }
}




//bydefault show the value of data i.e Apple inc.
document.body.onload = async()=>{

   companyName =  document.getElementById('comp').value

   rcvData = await  searchDATA(companyName)
 
    if(rcvData.status)
    {  
        mainData = await rcvData.data //main data is inside this variable coming from API
        showResult(mainData)
        
      
      
    }else
    {
        document.getElementsByClassName('result')[0].innerHTML ==''
       document.getElementsByClassName('result')[0].innerHTML =` <div class="alert alert-warning alert-dismissible fade show" role="alert">
       <strong>Ooops!</strong> ${rcvData.data}
       <button type="button" class="close" data-dismiss="alert" aria-label="Close">
         <span aria-hidden="true">&times;</span>
       </button>
     </div>`
    }


}

//select tag event mode..

selectData = document.getElementById('comp')

selectData.addEventListener('change',async(e)=>{
  
   Datarcvd = await  searchDATA(selectData.value)
   if(Datarcvd.status)
   {  
       mainData = await Datarcvd.data ////main data is inside this variable coming from API

       document.getElementById('company').innerText = selectData.value
       showResult(mainData)
       
     
     
   }else
   {
       document.getElementsByClassName('result')[0].innerHTML ==''
      document.getElementsByClassName('result')[0].innerHTML =` <div class="alert alert-warning alert-dismissible fade show" role="alert">
      <strong>Ooops!</strong> ${Datarcvd.data}
      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>`
   }


})

//input by user mode

document.getElementsByClassName('dosearch')[0].addEventListener('click',async()=>{

   userdata = document.getElementById('userinput').value.toUpperCase()

   if(userdata.length == 0){

    return
   }


   Datarcv = await  searchDATA(userdata)
   if(Datarcv.status)
   {  
       mainData = await Datarcv.data ////main data is inside this variable coming from API

       document.getElementById('company').innerText = userdata
       showResult(mainData)
       
     
     
   }else
   {
       document.getElementsByClassName('result')[0].innerHTML ==''
      document.getElementsByClassName('result')[0].innerHTML =` <div class="alert alert-warning alert-dismissible fade show" role="alert">
      <strong>Ooops!</strong> ${Datarcv.data}
      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button>
    </div>`
   }

   
})