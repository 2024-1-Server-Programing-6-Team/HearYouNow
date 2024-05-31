function navigate(page) {
    const contentArea = document.getElementById('main-content');

    let content = '';
    switch (page) {
        case 'deep-worry':
            content = '<h2>깊은 고민 상담소</h2><p>게시판이 들어가면 됩니다.</p>';
            break;
        case 'shallow-worry':
            content = '<h2>얕은 고민 상담소</h2><p>게시판이 들어가면 됩니다.</p>';
            break;
        default:
            content = '<h2>Welcome</h2><p>Select an option from the sidebar.</p>';
    }

    contentArea.innerHTML = content;
}

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('main-content');

    sidebar.classList.toggle('closed');
    mainContent.classList.toggle('expanded');
}

// 초기 로딩 시 메인 페이지 내용을 설정합니다.
document.addEventListener('DOMContentLoaded', () => navigate('calendar'));
