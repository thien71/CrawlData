// const searchInput = "";
// document.getElementById("myForm").addEventListener("submit", function(event) {
//     event.preventDefault(); // Ngăn chặn form gửi yêu cầu mặc định
//     const searchInput = document.getElementById("searchInput").value;
//     // Gọi API và xử lý dữ liệu
//     search(searchInput)
//     .then(data => {
//         console.log('Dữ liệu từ API:', data);
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// });

// async function search(searchInput) {
//     try {
//         console.log(searchInput);
//         const response = await fetch(`http://localhost:7000/search/?search_input=${searchInput}`);
//         if (!response.ok) {
//             throw new Error('Failed to fetch data');
//         }
//         const data = await response.json();
//         return data;
//     } catch (error) {
//         console.error('Error:', error);
//         throw error;
//     }
// }