
import { ApiRequest } from "../../functions/ApiRequest";
import { useEffect, useState } from "react";
import { Restaurante } from "../../types/Restaurante";

export const Home = () => {
    const [restaurante, setRestaurante] = useState<Restaurante[]>([]);

    useEffect(() => {
        ApiRequest<Restaurante[]>({
            url: "http://localhost:8000/cozinha/api/restaurante",
            type: "GET",
        }).then((response) => {
            if (response) {
                setRestaurante(response);
            }
        });
    }, []);

    return (    
        <div>
            <h1>Home</h1>
            {restaurante.map((restaurante) => (
                <div key={restaurante.id}>
                    <p>{restaurante.nome}</p>
                </div>
            ))}
        </div>
    );
}