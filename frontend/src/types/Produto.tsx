import { CategoriaProduto } from "./CategoriaProduto";

export type Produto = {
    id: number;
    preco: number;
    descricao: string;
    quantidade: number;
    imagem: string;
    ativo: boolean;
    categorias: CategoriaProduto[];
}