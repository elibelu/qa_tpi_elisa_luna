
describe('Caso 2: Agregar Producto y Verificación en el Carrito', () => {
    beforeEach(() => {
        // Logueo antes de cada test
        cy.visit('https://www.saucedemo.com/');
        cy.get('#user-name').type('standard_user');
        cy.get('#password').type('secret_sauce');
        cy.get('#login-button').click();
    });

    it('C3: Debería añadir el Sauce Labs Fleece Jacket al carrito y verificarlo', () => {
        const itemName = 'Sauce Labs Fleece Jacket';

        // 1. Encontrar y añadir el producto por su nombre
        cy.contains('.inventory_item_name', itemName)
          .parents('.inventory_item')
          .find('button.btn_primary')
          .click();

        // 2. Verificar que el contador del carrito se actualizó a 1
        cy.get('.shopping_cart_badge').should('have.text', '1');

        // 3. Ir al carrito
        cy.get('.shopping_cart_link').click();

        // 4. Verificar que el producto está en la página del carrito
        cy.url().should('include', '/cart.html');
        cy.get('.inventory_item_name').should('have.text', itemName);
    });
});