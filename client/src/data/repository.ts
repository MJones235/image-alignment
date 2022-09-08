import axios from "axios";

export class Repository {
  url = "http://127.0.0.1:5000";

  alignImages = async (template: string, image: string): Promise<any> => {
    try {
      const response = await axios.post(this.url, {
        template,
        image,
      });
      return response.data;
    } catch (e) {
      console.log(e);
      return {
        "aligned-image": null,
      };
    }
  };
}
