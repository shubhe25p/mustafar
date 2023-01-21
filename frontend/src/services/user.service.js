import axios from "axios";
class UserService{
    sendData(city, planet){
        return axios.post(process.env.REACT_APP_BASE_URL + {city, planet}).then(response => {
            return response.data;
        })
    }
}

export default new UserService();