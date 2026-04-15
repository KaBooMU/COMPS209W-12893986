async function getJSON(url, options = {}) {
  const response = await fetch(url, {
    headers: { "Content-Type": "application/json" },
    ...options
  });
  return response.json();
}

function formatMoney(value) {
  return `HKD ${Number(value).toFixed(2)}`;
}

async function loadMenu() {
  const menu = await getJSON("/api/menu");
  const filterValue = document.getElementById("menuFilter").value;
  const menuDiv = document.getElementById("menuList");
  menuDiv.innerHTML = "";

  const filtered = menu.filter(item => filterValue === "All" || item.type === filterValue);

  filtered.forEach(item => {
    const row = document.createElement("div");
    row.className = "list-row";
    row.innerHTML = `
      <div>
        <div class="item-title">${item.id} - ${item.name}</div>
        <div class="item-subtitle">${item.type} ${item.extra ? "| " + item.extra : ""} | ${formatMoney(item.price)}</div>
      </div>
      <button class="primary-btn small-btn">Add</button>
    `;
    row.querySelector("button").addEventListener("click", () => addItem(item.id));
    menuDiv.appendChild(row);
  });
}

async function loadTables() {
  const tables = await getJSON("/api/tables");
  const tablesDiv = document.getElementById("tableList");
  tablesDiv.innerHTML = "";

  tables.forEach(table => {
    const row = document.createElement("div");
    row.className = "list-row";
    row.innerHTML = `
      <div>
        <div class="item-title">Table ${table.number}</div>
        <div class="item-subtitle">Capacity: ${table.capacity}</div>
      </div>
      <div>${table.occupied ? "Occupied" : "Available"}</div>
    `;
    tablesDiv.appendChild(row);
  });
}

async function loadOrder() {
  const order = await getJSON("/api/order");
  const orderDiv = document.getElementById("orderList");
  const status = document.getElementById("orderStatus");

  if (!order) {
    orderDiv.innerHTML = '<div class="empty-text">No items in active order.</div>';
    status.textContent = "No active order.";
    document.getElementById("subtotal").textContent = "HKD 0.00";
    document.getElementById("serviceCharge").textContent = "HKD 0.00";
    document.getElementById("total").textContent = "HKD 0.00";
    return;
  }

  status.textContent = `Customer: ${order.customer_name} | Table: ${order.table_number} | Status: ${order.status}`;
  orderDiv.innerHTML = "";

  order.items.forEach((item, index) => {
    const row = document.createElement("div");
    row.className = "list-row";
    row.innerHTML = `
      <div>
        <div class="item-title">${item.name}</div>
        <div class="item-subtitle">${formatMoney(item.price)}</div>
      </div>
      <button class="danger-btn small-btn">Remove</button>
    `;
    row.querySelector("button").addEventListener("click", () => removeItem(index));
    orderDiv.appendChild(row);
  });

  document.getElementById("subtotal").textContent = formatMoney(order.subtotal);
  document.getElementById("serviceCharge").textContent = formatMoney(order.service_charge);
  document.getElementById("total").textContent = formatMoney(order.total);
}

async function loadHistory() {
  const history = await getJSON("/api/history");
  const historyDiv = document.getElementById("historyBox");
  historyDiv.innerHTML = "";

  if (!history || history.length === 0) {
    historyDiv.innerHTML = '<div class="empty-text">No saved order history.</div>';
    return;
  }

  history.forEach(entry => {
    const row = document.createElement("div");
    row.className = "history-entry";
    row.innerHTML = `
      <strong>${entry.customer_name}</strong><br>
      <span>${entry.items.join(", ")}</span><br>
      <span>${entry.total_line}</span>
    `;
    historyDiv.appendChild(row);
  });
}

async function createOrder() {
  const name = document.getElementById("customerName").value.trim();
  const phone = document.getElementById("customerPhone").value.trim();
  const people = document.getElementById("groupSize").value;

  const result = await getJSON("/api/create_order", {
    method: "POST",
    body: JSON.stringify({ name, phone, people })
  });

  if (result.error) {
    alert(result.error);
  }
  await refreshAll();
}

async function addItem(itemId) {
  const result = await getJSON("/api/add_item", {
    method: "POST",
    body: JSON.stringify({ item_id: itemId })
  });
  if (result.error) {
    alert(result.error);
  }
  await loadOrder();
}

async function removeItem(index) {
  const result = await getJSON("/api/remove_item", {
    method: "POST",
    body: JSON.stringify({ index })
  });
  if (result.error) {
    alert(result.error);
  }
  await loadOrder();
}

async function saveOrder() {
  const result = await getJSON("/api/save_order", { method: "POST" });
  if (result.error) {
    alert(result.error);
  } else {
    alert(result.message);
  }
  await loadHistory();
}

async function checkout() {
  const result = await getJSON("/api/checkout", { method: "POST" });
  if (result.error) {
    alert(result.error);
  } else {
    alert(result.message);
  }
  await refreshAll();
}

async function clearDisplay() {
  document.getElementById("customerName").value = "";
  document.getElementById("customerPhone").value = "";
  document.getElementById("groupSize").value = 2;
  await loadOrder();
}

async function refreshAll() {
  await loadMenu();
  await loadTables();
  await loadOrder();
  await loadHistory();
}

document.getElementById("createOrderBtn").addEventListener("click", createOrder);
document.getElementById("saveOrderBtn").addEventListener("click", saveOrder);
document.getElementById("checkoutBtn").addEventListener("click", checkout);
document.getElementById("clearOrderBtn").addEventListener("click", clearDisplay);
document.getElementById("refreshHistoryBtn").addEventListener("click", loadHistory);
document.getElementById("menuFilter").addEventListener("change", loadMenu);

refreshAll();
