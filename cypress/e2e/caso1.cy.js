
describe('Caso 1: Login Exitoso y Verificación de Ordenamiento', () => {
    beforeEach(() => {
        // Visitar la página antes de cada test
        cy.visit('https://www.saucedemo.com/');
    });

    it('C1: Debería iniciar sesión correctamente con standard_user y verificar orden A-Z', () => {
        // 1. Ingresar credenciales y loguearse
        cy.get('#user-name').type('standard_user');
        cy.get('#password').type('secret_sauce');
        cy.get('#login-button').click();

        // 2. Verificar que el logueo fue exitoso
        cy.url().should('include', '/inventory.html');
        cy.get('.title').should('have.text', 'Products');

        // 3. Verificar orden A-Z (por defecto)
        // El primer elemento debe ser 'Sauce Labs Backpack'
        cy.get('.inventory_item_name').first().should('have.text', 'Sauce Labs Backpack');
    });

    it('C2: Debería verificar el orden Z-A', () => {
        // Logueo rápido
        cy.get('#user-name').type('standard_user');
        cy.get('#password').type('secret_sauce');
        cy.get('#login-button').click();

        // 4. Cambiar orden a Z-A
        cy.get('.product_sort_container').select('Name (Z to A)');

        // 5. Verificar que el primer elemento es el último de la lista: 'Test.allTheThings() T-Shirt (Red)'
        cy.get('.inventory_item_name').first().should('have.text', 'Test.allTheThings() T-Shirt (Red)');
    });
});