import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    const fetchPatients = async () => {
      
      try {
        const response = await axios.get('https://gosh-synth-fhir.azurehealthcareapis.com/Patient', {
          headers: {
            'Authorization': `Bearer ${import.meta.env.VITE_TOKEN}`,
            'Content-Type': 'application/fhir+json'
          }
        });
        setPatients(response.data.entry);
      } catch (error) {
        console.error(`Error fetching patients: ${error}`);
      }
    };

    fetchPatients();
  }, []);

  return (
    <div className="App">
      {patients && patients.map((patient, index) => (
        <div key={index}>
          <h2>{patient.resource.name[0].given.join(' ')} {patient.resource.name[0].family}</h2>
          <p>Gender: {patient.resource.gender}</p>
          <p>Birth Date: {patient.resource.birthDate}</p>
          {/* Add more fields as needed */}
        </div>
      ))}
    </div>
  );
}

export default App;