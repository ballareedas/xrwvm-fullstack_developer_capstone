import React, { useState, useEffect, useCallback } from 'react';
import { useParams } from 'react-router-dom';
import "./Dealers.css";
import "../assets/style.css";
import Header from '../Header/Header';


const PostReview = () => {
  const [dealer, setDealer] = useState({});
  const [review, setReview] = useState("");
  const [model, setModel] = useState();
  const [year, setYear] = useState("");
  const [date, setDate] = useState("");
  const [carmodels, setCarmodels] = useState([]);

  let curr_url = window.location.href;
  let root_url = curr_url.substring(0,curr_url.indexOf("postreview"));
  let params = useParams();
  let id =params.id;
  let dealer_url = root_url+`djangoapp/dealer/${id}`;
  let review_url = root_url+`djangoapp/add_review`;
  let carmodels_url = root_url+`djangoapp/get_cars`;

  const postreview = async () => {
  let name = sessionStorage.getItem("firstname") + " " + sessionStorage.getItem("lastname");
  
  // If the first and second name are stored as null, use the username
  if (name.includes("null")) {
    name = sessionStorage.getItem("username");
  }

  if (!model || review.trim() === "" || date === "" || year === "" || model === "") {
    alert("All details are mandatory");
    return;
  }

  // Safer delimiter for make and model
  let [make_chosen, model_chosen] = model.split("::"); // <-- Update your select to use "::" as delimiter

  let jsoninput = JSON.stringify({
  name: name,
  dealership: parseInt(id),
  review: review,
  purchase: true,
  purchase_date: date,
  car_make: make_chosen,
  car_model: model_chosen,
  car_year: parseInt(year),
});


  console.log("Review being posted:", jsoninput);

  try {
    const res = await fetch(review_url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: jsoninput,
    });

    const json = await res.json();
    console.log("Response from backend:", res.status, json);

    if (res.status === 200 && json.status === 200) {
      window.location.href = window.location.origin + "/dealer/" + id;
    } else {
      alert("Failed to post review. Server response: " + (json.message || "Unknown error"));
    }

  } catch (err) {
    console.error("Error occurred while posting review:", err);
    alert("Network error. Please try again later.");
  }
};

  const get_dealer = useCallback(async ()=>{
    const res = await fetch(dealer_url, {
      method: "GET"
    });
    const retobj = await res.json();
    
    if(retobj.status === 200) {
      let dealerobjs = Array.from(retobj.dealer)
      if(dealerobjs.length > 0)
        setDealer(dealerobjs[0])
    }
  },[dealer_url]);

  const get_cars = useCallback(async ()=>{
    const res = await fetch(carmodels_url, {
      method: "GET"
    });
    const retobj = await res.json();
    
    let carmodelsarr = Array.from(retobj.CarModels)
    setCarmodels(carmodelsarr)
  },[carmodels_url]);
  
  useEffect(() => {
    get_dealer();
    get_cars();
  },[get_dealer , get_cars]);


  return (
    <div>
      <Header/>
      <div  style={{margin:"5%"}}>
      <h1 style={{color:"darkblue"}}>{dealer.full_name}</h1>
      <textarea id='review' cols='50' rows='7' onChange={(e) => setReview(e.target.value)}></textarea>
      <div className='input_field'>
      Purchase Date <input type="date" onChange={(e) => setDate(e.target.value)}/>
      </div>
      <div className='input_field'>
      Car Make 
      {/* <select name="cars" id="cars" onChange={(e) => setModel(e.target.value)}>
      <option value="" selected disabled hidden>Choose Car Make and Model</option>
      {carmodels.map(carmodel => (
          <option value={carmodel.CarMake+" "+carmodel.CarModel}>{carmodel.CarMake} {carmodel.CarModel}</option>
      ))}
      </select>   */}

      <select name="cars" id="cars" onChange={(e) => setModel(e.target.value)}>
      <option value="" selected disabled hidden>Choose Car Make and Model</option>
      {carmodels.map(carmodel => (
        <option value={`${carmodel.CarMake}::${carmodel.CarModel}`} key={`${carmodel.CarMake}-${carmodel.CarModel}`}>
          {carmodel.CarMake} {carmodel.CarModel}
        </option>
      ))}
      </select>

      </div >

      <div className='input_field'>
      Car Year <input type="int" onChange={(e) => setYear(e.target.value)} max={2023} min={2015}/>
      </div>

      <div>
      <button className='postreview' onClick={postreview}>Post Review</button>
      </div>
    </div>
    </div>
  )
}
export default PostReview
