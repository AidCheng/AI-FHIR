import React from 'react';
import PatientList from './components/PatientList';

const App = () => {
  return (
    <div className="App">
      <h1>FHIR Patient Data</h1>
      <PatientList />
    </div>
  );
}

export default App;
