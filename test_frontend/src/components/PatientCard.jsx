import React from "react";

const PatientCard = ({ patient }) => {
  return (
    <div className="patient-card">
      {patient.patient_details.map((patient, index) => (
        <div key={index}>
          <h2>Name: {patient.name}</h2>
          <p>Birth Date: {patient.birthDate}</p>
          <p>Gender: {patient.gender}</p>
        </div>
      ))}
      <h3>Conditions:</h3>
      {patient.conditions.map((condition, index) => (
        <div key={index}>
          <p>Condition: {condition.conditionName}</p>
          <p>Duration: {condition.duration}</p>
        </div>
      ))}
      <h3>Observations:</h3>
      {patient.observations.map((observation, index) => (
        <div key={index}>
          <p>Observation Type: {observation.observationType}</p>
          <p>Value: {observation.value}</p>
          <p>Date: {observation.date}</p>
        </div>
      ))}
    </div>
  );
};

export default PatientCard;
