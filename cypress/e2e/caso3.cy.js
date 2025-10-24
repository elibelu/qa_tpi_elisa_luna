
describe('Caso 3: Remover Producto y Flujo de Checkout', () => {
    beforeEach(() => {
        // Logueo antes de cada test y añadir un producto
        cy.visit('https://www.saucedemo.com/');
        cy.get('#user-name').type('standard_user');
        cy.get('#password').type('secret_sauce');
        cy.get('#login-button').click();
        
        // Añadir dos productos para el flujo de test
        cy.get('#add-to-cart-sauce-labs-backpack').click();
        cy.get('#add-to-cart-sauce-labs-bike-light').click();
        cy.get('.shopping_cart_link').click();
    });

    it('C4: Debería remover un producto del carrito y completar el checkout', () => {
        // 1. Verificar que hay dos productos
        cy.get('.cart_item').should('have.length', 2);

        // 2. Remover el primer producto (Sauce Labs Backpack)
        cy.get('.cart_item')
          .first()
          .find('.btn_secondary') 
          .click();

        // 3. Verificar que solo queda un producto en el carrito
        cy.get('.cart_item').should('have.length', 1);

        // 4. Iniciar el checkout
        cy.get('#checkout').click();

        // 5. Llenar la información del formulario
        cy.get('#first-name').type('Elisa');
        cy.get('#last-name').type('Luna');
        cy.get('#postal-code').type('1753');

        // 6. Continuar
        cy.get('#continue').click();

        // 7. Verificar la página de resumen (Overview)
        cy.url().should('include', '/checkout-step-two.html');
        cy.get('.summary_total_label').should('contain', 'Total:'); 

        // 8. Finalizar la compra
        cy.get('#finish').click();

        // 9. Verificar el mensaje de éxito
        cy.url().should('include', '/checkout-complete.html');
        cy.get('.complete-header').should('have.text', 'Thank you for your order!');
    });
});