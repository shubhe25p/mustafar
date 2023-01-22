import axios from "axios";
class UserService{
    sendData(city, planet){
        const data = {
            city: city,
            planet: planet
        }
        return axios.post(process.env.REACT_APP_BASE_URL, data).then(response => {
            return response.data;
        })
    }
}

export default new UserService();