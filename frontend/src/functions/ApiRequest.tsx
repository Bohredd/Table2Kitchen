import axios, { AxiosRequestConfig } from "axios";

interface ApiRequestProps {
  url: string;
  type: "GET" | "POST" | "PUT" | "DELETE";
  id?: string;
  headers?: Record<string, string>;
  data?: Record<string, unknown>;
}

export const ApiRequest = async <T,>({
  url,
  type,
  id,
  headers,
  data,
}: ApiRequestProps): Promise<T | null> => {
  try {
    const config: AxiosRequestConfig = {
      method: type,
      url: url,
      headers: headers || {},
      data: id ? { id, ...data } : data,
    };

    const response = await axios(config);
    return response.data as T; 
  } catch (error) {
    console.error("API Request failed:", error);
    return null; 
  }
};
