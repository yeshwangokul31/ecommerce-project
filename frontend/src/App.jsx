
import React, { useEffect, useState } from 'react';

function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch('/api/products')
      .then(response => {
        if (!response.ok) {
          throw new Error('Unable to fetch products');
        }
        return response.json();
      })
      .then(data => setProducts(data))
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="container">
      <h1>My E-Commerce Store</h1>
      <p>Welcome to our online shopping application.</p>

      <h2>Available Products</h2>

      {loading && <p>Loading products...</p>}
      {error && <p className="error">{error}</p>}

      <div className="products">
        {products.map(product => (
          <div className="product" key={product.id}>
            <h3>{product.name}</h3>
            <p>{product.description}</p>
            <strong>₹{product.price}</strong>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
