

let cName =  document.getElementById('comps');//company name 
var dataTobeInsert = document.getElementsByClassName('tablebody')[0];//data to be insert



cName.onchange = ()=>{

   
    insertIntable()
  
    
}



//this function will insert in the table according to selected company
function insertIntable(){
    let companyName =  document.getElementsByClassName('cnames')[0]
   
    if(cName.value== '500112' )
    {
        companyName.innerText = 'STATE BANK OF INDIA 500112'
 
        dataTobeInsert.innerHTML = `
        <tr>
            
             <td>29/04/2022</td>
             <td>507.5</td>
             <td>512.45</td>
             <td>494.15</td>
             <td>496.5</td>
             <td>400939</td>
           </tr>
           <tr>
        
             <td>28/04/2022</td>
             <td>499.7</td>
             <td>509.9</td>
             <td>496.5</td>
             <td>507.05</td>
             <td>347902</td>
           </tr>
           <tr>
            
             <td>27/04/2022</td>
             <td>500</td>
             <td>503</td>
             <td>491.85</td>
             <td>497</td>
             <td>626412</td>
           </tr>
           <tr>
            
             <td>26/04/2022</td>
             <td>499.6</td>
             <td>510</td>
             <td>499.25</td>
             <td>506</td>
             <td>321411</td>
           </tr>
          
           <tr>
            
             <td>25/04/2022</td>
             <td>496</td>
             <td>499.15</td>
             <td>490</td>
             <td>494.7</td>
             <td>386460</td>
           </tr>
        
        
        `
 
        
 
    }
    else if(cName.value== '500111')
    {
 
     companyName.innerText = 'RELIANCE CAPITAL LTD. 500111'
 
 
     dataTobeInsert.innerHTML = `
     <tr>
         
          <td>30/03/2022</td>
          <td>16.36</td>
          <td>16.36</td>
          <td>16.36</td>
          <td>16.36</td>
          <td>265736</td>
        </tr>
        <tr>
     
          <td>29/03/2022</td>
          <td>15.59</td>
          <td>15.59</td>
          <td>15.59</td>
          <td>15.59</td>
          <td>83572</td>
        </tr>
        <tr>
         
          <td>28/03/2022</td>
          <td>14.85</td>
          <td>14.85</td>
          <td>14.85</td>
          <td>14.85</td>
          <td>78665</td>
        </tr>
        <tr>
         
          <td>25/03/2022</td>
          <td>13.9</td>
          <td>14.58</td>
          <td>13.9</td>
          <td>14.15</td>
          <td>795129</td>
        </tr>
       
        <tr>
         
          <td>24/03/2022</td>
          <td>13.7</td>
          <td>14.1</td>
          <td>13.62</td>
          <td>13.89</td>
          <td>607932</td>
        </tr>
     
     
     `
 
    }
    else if(cName.value== '500820')
    {
 
     companyName.innerText = 'ASIAN PAINTS LTD. 500820'
 
     dataTobeInsert.innerHTML = `
     <tr>
         
          <td>29/04/2022</td>
          <td>3250</td>
          <td>3276.55</td>
          <td>3220.75</td>
          <td>3239.3</td>
          <td>106143</td>
        </tr>
        <tr>
     
          <td>28/04/2022</td>
          <td>3183</td>
          <td>3267</td>
          <td>3170.05</td>
          <td>3248.3</td>
          <td>117108</td>
        </tr>
        <tr>
         
          <td>27/04/2022</td>
          <td>3100</td>
          <td>3164.6</td>
          <td>3085</td>
          <td>3148.3</td>
          <td>26346</td>
        </tr>
        <tr>
         
          <td>26/04/2022</td>
          <td>3116</td>
          <td>3150.1</td>
          <td>3107</td>
          <td>3125.6</td>
          <td>36762</td>
        </tr>
       
        <tr>
         
          <td>25/04/2022</td>
          <td>3105</td>
          <td>3155</td>
          <td>3095.15</td>
          <td>3130.05</td>
          <td>79066</td>
        </tr>
     
     
     `
 
    }
    else if(cName.value== '512599')
    {
 
     companyName.innerText = 'ADANI ENTERPRISES LTD. 512599'
 
     dataTobeInsert.innerHTML = `
     <tr>
         
          <td>29/04/2022</td>
          <td>2389</td>
          <td>2394</td>
          <td>2301.9</td>
          <td>2333.1</td>
          <td>174534</td>
        </tr>
        <tr>
     
          <td>28/04/2022</td>
          <td>2352</td>
          <td>2389.75</td>
          <td>2336.65</td>
          <td>2378.9</td>
          <td>101337</td>
        </tr>
        <tr>
         
          <td>27/04/2022</td>
          <td>2405</td>
          <td>2420</td>
          <td>2326</td>
          <td>2334.6</td>
          <td>166481</td>
        </tr>
        <tr>
         
          <td>26/04/2022</td>
          <td>2303.9</td>
          <td>2419.7</td>
          <td>2294.85</td>
          <td>2397</td>
          <td>253308</td>
        </tr>
       
        <tr>
         
          <td>25/04/2022</td>
          <td>2260</td>
          <td>2298.45</td>
          <td>2241.55</td>
          <td>2287.2</td>
          <td>198294</td>
        </tr>
     
     
     `
 
    }
    else if(cName.value== '500180')
    {
 
     companyName.innerText = 'HDFC Bank Ltd 500180'
 
 
     dataTobeInsert.innerHTML = `
     <tr>
         
          <td>29/04/2022</td>
          <td>1379.9</td>
          <td>1404.7</td>
          <td>1372</td>
          <td>1384.75</td>
          <td>226194</td>
        </tr>
        <tr>
     
          <td>28/04/2022</td>
          <td>1375</td>
          <td>1375.8</td>
          <td>1362</td>
          <td>1371.05</td>
          <td>250493</td>
        </tr>
        <tr>
         
          <td>27/04/2022</td>
          <td>1360</td>
          <td>1378.3</td>
          <td>1355.25</td>
          <td>1372.65</td>
          <td>359986</td>
        </tr>
        <tr>
         
          <td>26/04/2022</td>
          <td>1374.8</td>
          <td>1383.8</td>
          <td>1357.15</td>
          <td>1372.35</td>
          <td>198963</td>
        </tr>
       
        <tr>
         
          <td>25/04/2022</td>
          <td>1352.6</td>
          <td>1370.7</td>
          <td>1323.9</td>
          <td>1365.55</td>
          <td>274235</td>
        </tr>
     
     
     `
 
    }
    else if(cName.value== '532343')
    {
 
     companyName.innerText = 'TVS MOTOR COMPANY LTD. 532343'
 
     dataTobeInsert.innerHTML = `
     <tr>
         
          <td>29/04/2022</td>
          <td>679</td>
          <td>686.25</td>
          <td>651.1</td>
          <td>655.1</td>
          <td>70289</td>
        </tr>
        <tr>
     
          <td>28/04/2022</td>
          <td>693.3</td>
          <td>693.65</td>
          <td>677.85</td>
          <td>680.85</td>
          <td>60455</td>
        </tr>
        <tr>
         
          <td>27/04/2022</td>
          <td>676.25</td>
          <td>689.95</td>
          <td>671.75</td>
          <td>686.65</td>
          <td>91272</td>
        </tr>
        <tr>
         
          <td>26/04/2022</td>
          <td>664</td>
          <td>683.85</td>
          <td>655.55</td>
          <td>682.15</td>
          <td>145736</td>
        </tr>
       
        <tr>
         
          <td>25/04/2022</td>
          <td>646.8</td>
          <td>654</td>
          <td>637.45</td>
          <td>649.3</td>
          <td>11402</td>
        </tr>
     
     
     `
    }
    else if(cName.value== '542830')
    {
 
     companyName.innerText = 'Indian Railway Catering and Tourism Corporation Ltd 542830'
     dataTobeInsert.innerHTML = `
     <tr>
         
          <td>29/04/2022</td>
          <td>761</td>
          <td>766.15</td>
          <td>745</td>
          <td>746.3</td>
          <td>75795</td>
        </tr>
        <tr>
     
          <td>28/04/2022</td>
          <td>760.9</td>
          <td>760.9</td>
          <td>744.15</td>
          <td>757.15</td>
          <td>73677</td>
        </tr>
        <tr>
         
          <td>27/04/2022</td>
          <td>757.7</td>
          <td>758.55</td>
          <td>742</td>
          <td>748.2</td>
          <td>78576</td>
        </tr>
        <tr>
         
          <td>26/04/2022</td>
          <td>749</td>
          <td>762.5</td>
          <td>749</td>
          <td>760.95</td>
          <td>63055</td>
        </tr>
       
        <tr>
         
          <td>25/04/2022</td>
          <td>749</td>
          <td>754</td>
          <td>740.5</td>
          <td>745.45</td>
          <td>70086</td>
        </tr>
     
     
     `
    }
    else if(cName.value== '543320')
    {
 
     companyName.innerText = 'Zomato Ltd 543320'
     dataTobeInsert.innerHTML = `
     <tr>
         
          <td>29/04/2022</td>
          <td>74.65</td>
          <td>74.8</td>
          <td>71.15</td>
          <td>71.7</td>
          <td>1545342</td>
        </tr>
        <tr>
     
          <td>28/04/2022</td>
          <td>77.3</td>
          <td>77.55</td>
          <td>73.5</td>
          <td>73.85</td>
          <td>2658903</td>
        </tr>
        <tr>
         
          <td>27/04/2022</td>
          <td>79.45</td>
          <td>79.55</td>
          <td>75.55</td>
          <td>75.9</td>
          <td>7852471</td>
        </tr>
        <tr>
         
          <td>26/04/2022</td>
          <td>80.8</td>
          <td>80.8</td>
          <td>78.55</td>
          <td>79.6</td>
          <td>947703</td>
        </tr>
       
        <tr>
         
          <td>25/04/2022</td>
          <td>80.95</td>
          <td>81.65</td>
          <td>78.5</td>
          <td>78.75</td>
          <td>1212098</td>
        </tr>
     
     
     `
    }
    else if(cName.value== '532371')
    {
 
     companyName.innerText = 'TATA TELESERVICES (MAHARASHTRA) LTD. 532371'
     dataTobeInsert.innerHTML = `
     <tr>
         
          <td>29/04/2022</td>
          <td>145</td>
          <td>150</td>
          <td>139.55</td>
          <td>139.6</td>
          <td>838189</td>
        </tr>
        <tr>
     
          <td>28/04/2022</td>
          <td>150.5</td>
          <td>156.9</td>
          <td>145.65</td>
          <td>146.85</td>
          <td>1253319</td>
        </tr>
        <tr>
         
          <td>27/04/2022</td>
          <td>163</td>
          <td>165.9</td>
          <td>151.8</td>
          <td>153.3</td>
          <td>1915403</td>
        </tr>
        <tr>
         
          <td>26/04/2022</td>
          <td>155.8</td>
          <td>167.1</td>
          <td>151.2</td>
          <td>159.65</td>
          <td>1668277</td>
        </tr>
       
        <tr>
         
          <td>25/04/2022</td>
          <td>161.5</td>
          <td>163.65</td>
          <td>159.15</td>
          <td>159.15</td>
          <td>511184</td>
        </tr>
     `
     
    }
    else if(cName.value== '540376')
    {
 
     companyName.innerText = 'Avenue Supermarts Ltd 540376'
     dataTobeInsert.innerHTML = `
     <tr>
         
          <td>29/04/2022</td>
          <td>4030</td>
          <td>4083.95</td>
          <td>3909.45</td>
          <td>3948.6</td>
          <td>28673</td>
        </tr>
        <tr>
     
          <td>28/04/2022</td>
          <td>3999.7</td>
          <td>4052</td>
          <td>3997</td>
          <td>4025.5</td>
          <td>28082</td>
        </tr>
        <tr>
         
          <td>27/04/2022</td>
          <td>4024</td>
          <td>4024</td>
          <td>3962</td>
          <td>3977.8</td>
          <td>6848</td>
        </tr>
        <tr>
         
          <td>26/04/2022</td>
          <td>3998</td>
          <td>4048</td>
          <td>3996.05</td>
          <td>4040.75</td>
          <td>9090</td>
        </tr>
       
        <tr>
         
          <td>25/04/2022</td>
          <td>4013.95</td>
          <td>4021</td>
          <td>3977</td>
          <td>3988.75</td>
          <td>7937</td>
        </tr>
     `
    }else{
        companyName.innerText = 'Unknown'
    }
}



try{


  document.body.onload = function(){

    cName.value = document.getElementsByClassName('Ccode')[0].innerText
    insertIntable()

  }

}catch(e){

}